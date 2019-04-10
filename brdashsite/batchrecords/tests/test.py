from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from users.models import CustomUser
from ..models import Product, BatchRecord

def setUp(self):
	product = Product.objects.create(
		id = 12345678901,
		description = "testing product",
		family = 1,
	)
	user = CustomUser.objects.create(
		username = 'johndoe',
		password = '1234',
		email = 'johndoe@johndoe.com',
		first_name = 'john',
		last_name = 'doe',
	)
	BatchRecord.objects.create(
		product = product,
		lot = "1234567890",
		workorder = "1234567",
		expiration_date = timezone.now() + timezone.timedelta(days=365),
		created_by = user,
		updated_by = user,
	)
	self.url = reverse('batchrecords:create')
	self.response = self.client.get(self.url)


class LoginRequiredCreateBatchRecordTests(TestCase):
	setUp()
	# def setUp(self):
		# product = Product.objects.create(
			# id = 12345678901,
			# description = "testing product",
			# family = 1,
		# )
		# user = CustomUser.objects.create(
			# username = 'johndoe',
			# password = '1234',
			# email = 'johndoe@johndoe.com',
			# first_name = 'john',
			# last_name = 'doe',
		# )
		# BatchRecord.objects.create(
			# product = product,
			# lot = "1234567890",
			# workorder = "1234567",
			# expiration_date = timezone.now() + timezone.timedelta(days=365),
			# created_by = user,
			# updated_by = user,
		# )
		# self.url = reverse('batchrecords:create')
		# self.response = self.client.get(self.url)
	
	def test_redirection(self):
		login_url = reverse('login')
		self.assertRedirects(self.response,'{login_url}?next={url}'.format(login_url=login_url, url=self.url))

""" Test to make sure correct status change select opions are showing	
# class UpdateBatchRecordStatusTests(TestCase):
	# def
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	