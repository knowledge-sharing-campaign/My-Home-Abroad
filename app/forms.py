from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	phone_no = forms.IntegerField(required=True)
	nationality = forms.CharField(required=True)
	DOB = forms.CharField(required=True)
	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'phone_no',
			'DOB',
			'nationality',
			'password1',
			'password2',
			)
	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.first_name = ('')
		user.last_name = ('')
		user.email = ('')
		user.DOB = ('')
		user.nationality = ('') 

		if commit:
			user.save()

		return user 