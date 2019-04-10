import datetime

from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from users.models import CustomUser


class Product(models.Model):
	FAMILY_CHOICES = (
		(1, 'red'),
		(2, 'white'),
		(3, 'blue'),
	)
	
	id = models.IntegerField("part number", primary_key=True) # need to add validator for 11 chars
	# alt_id = models.IntegerField() need to add for another ID
	description = models.CharField(max_length=30)
	family = models.IntegerField(choices=FAMILY_CHOICES)
	total_target_time = models.DurationField(default=datetime.timedelta(days=1))
	target_duration_1 = models.DurationField(default=datetime.timedelta(days=1))
	target_duration_2 = models.DurationField(default=datetime.timedelta(days=2))
	target_duration_3 = models.DurationField(default=datetime.timedelta(days=3))
	target_duration_4 = models.DurationField(default=datetime.timedelta(days=4))
	target_duration_5 = models.DurationField(default=datetime.timedelta(days=5))
	
	def __str__(self):
		return str(self.id)
		

class BatchRecord(models.Model):
	STATUS_CHOICES = [
		(1, 'Creation'),
		(2, 'Ready'),
		(3, 'In Production'),
		(4, 'Tier 1 Review'),
		(5, 'Tier 2 Review'),
		(6, 'Complete'),
	]
	
	product = models.ForeignKey(Product, on_delete=models.PROTECT)
	lot = models.CharField(max_length=10, help_text="10 alphanumeric characters or less")
	workorder = models.CharField(max_length=7)
	manufacture_date = models.DateField(default=timezone.now, help_text="YYYY-MM-DD")
	expiration_date = models.DateField(help_text="YYYY-MM-DD")
	created_at = models.DateTimeField(auto_now_add=True, editable=False) # set to current time when object is created 
	created_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="createuser")
	updated_at = models.DateTimeField(auto_now=True) # set to current time when object is saved
	updated_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="updateuser")
	current_status = models.IntegerField(choices=STATUS_CHOICES, blank=False, default=1)
	status_changes = models.IntegerField(default=0)
	
	def __str__(self):
		return str(self.lot)

	class Meta:
		unique_together = (("product", "lot"),)
		ordering = ["-updated_at"]
	
	def get_target_completion_datetime(self):
		target_completion_datetime = self.product.total_target_time + self.updated_at
		return target_completion_datetime
		
	def get_seconds_to_target(self):
		target_completion_datetime = self.product.total_target_time + self.updated_at
		timedelta_to_target = target_completion_datetime - timezone.now()
		seconds_to_target = timedelta_to_target.total_seconds()
		return int(seconds_to_target)
	
	def log_batch_record_history(self, new_status, new_time): 
		if new_status != self.current_status:
			BatchRecordHistory(
				batchrecord=self,
				status=self.current_status,
				timestamp_start=self.updated_at,
				timestamp_end=new_time,
				duration=new_time-self.updated_at,
				updated_by=self.updated_by,
			).save()
		

class BatchRecordHistory(models.Model):
	STATUS_CHOICES = BatchRecord.STATUS_CHOICES
	batchrecord = models.ForeignKey(BatchRecord, related_name='history', on_delete=models.PROTECT)
	status = models.IntegerField(choices=STATUS_CHOICES, blank=False)
	timestamp_start = models.DateTimeField()
	timestamp_end = models.DateTimeField()
	duration = models.DurationField(default=datetime.timedelta(days=2))
	updated_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="updatehistoryuser")
	
	def __str__(self):
		return str(self.batchrecord)
	
	class Meta:
		ordering = ('timestamp_start',)
