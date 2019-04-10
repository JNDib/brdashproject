from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
	email = forms.CharField(max_length=100, required=True, widget=forms.EmailInput())
	first_name = forms.CharField(max_length=100, required=True)
	last_name = forms.CharField(max_length=100, required=True)
	
	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('username', 'email', 'first_name', 'last_name')
		
		
class CustomUserChangeForm(UserChangeForm):
	
	
	class Meta:
		model = CustomUser
		fields = ('username', 'email', 'first_name', 'last_name')
