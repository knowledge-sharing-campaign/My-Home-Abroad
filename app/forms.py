from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from . models import Volunteer, BookNow
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

class VolunteerForm(UserCreationForm):
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
		user = super(VolunteerForm, self).save(commit=False)
		user.first_name = ('first_name')
		user.last_name = ('last_name')
		user.email = ('email')
		user.DOB = ('DOB')
		user.nationality = ('nationality')

		if commit:
		 user.save()

		return user

class BookNowForm(forms.ModelForm):
	
	class Meta:
		model = BookNow
		fields = (
			'first_name',
			'last_name',
			'gender',
			'age', 
			'email',
			'nationality',
			'number_of_Adult_travellers',
			'number_of_Children_travellers',
			'travelling_From',
			'travelling_To',
			'arrival_city',
			'arrival_date',
			)

	def save(self, commit=True):
		user = super(BookNowForm, self).save()
		
		if commit:
		 user.save()

		return user