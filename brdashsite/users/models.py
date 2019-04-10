from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
	# add additional fields in here if required
	
	def __str__(self):
		return self.username

