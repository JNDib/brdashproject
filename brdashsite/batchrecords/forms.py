from django import forms

from .models import BatchRecord

CHOICES = BatchRecord.STATUS_CHOICES
	
def get_current_status_choices(object_id):
	if BatchRecord.objects.get(pk=object_id).current_status == 1:
		return [CHOICES[1]]
	elif BatchRecord.objects.get(pk=object_id).current_status == 2:
		return [CHOICES[2]]
	elif BatchRecord.objects.get(pk=object_id).current_status == 3:
		return [CHOICES[3]]
	elif BatchRecord.objects.get(pk=object_id).current_status == 4:
		return [CHOICES[4]]
	elif BatchRecord.objects.get(pk=object_id).current_status == 5:
		return [CHOICES[3], CHOICES[5]]
	elif BatchRecord.objects.get(pk=object_id).current_status == 6:
		return []
	else:
		return CHOICES


class BatchRecordCreateForm(forms.ModelForm):
	class Meta:
		model = BatchRecord
		fields = ['workorder', 'product', 'lot', 'manufacture_date', 'expiration_date']


class BatchRecordChangeStatusForm(forms.ModelForm):
	current_status = forms.ChoiceField(choices=CHOICES)
	
	class Meta:
		model = BatchRecord
		fields = ['current_status']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		current_status = None
		if 'current_status' in self.data:
			try:
				current_status = int(self.data.get('current_status'))
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			current_status = self.instance.current_status
			
		if current_status is not None:
			self.fields['current_status'].choices = get_current_status_choices(self.instance.pk)
	
		

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		