from django import forms
from django.forms import ModelForm
from app.models import BookNow
from django.contrib.auth.models import User
from . models import Volunteer
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
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	gender = forms.CharField(required=True)
	age = forms.IntegerField(required=True)
	email = forms.EmailField(required=True)
	nationality = forms.CharField(required=True)
	number_of_Adult_travellers = forms.IntegerField(required=True)
	number_of_Children_travellers = forms.IntegerField(required=True)
	travelling_From = forms.CharField(required=True)
	travelling_To = forms.CharField(required=True)
	arrival_city = forms.CharField(max_length=40)
	arrival_date = forms.DateField(required=True)
	class Meta:
		model = User
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
		user = super(BookNowForm, self).save(commit=False)
		user.first_name = ('first_name')
		user.last_name = ('last_name')
		user.gender = ('gender')
		user.DOB = ('DOB')
		user.email = ('email')
		user.nationality = ('nationality')
		user.number_of_Adult_travellers = ('number_of_Adult_travellers')
		user.number_of_Children_travellers = ('number_of_Children_travellers')
		user.travelling_From = ('travelling_From')
		user.travelling_To = ('travelling_To')
		user.arrival_city = ('arrival_city')
		user.arrival_date = ('arrival_date')

		if commit:
		 users.save()

		return user

