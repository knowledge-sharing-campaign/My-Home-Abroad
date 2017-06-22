from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from . models import Volunteer, BookNow, Register
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(forms.ModelForm):
	class Meta:
		model = Register
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'birth_date',
			'gender',
			'phone',
            'nationality',
			'password',
			'conform_password',
			)
	def save(self, commit=True):
		user = super(RegisterForm, self).save()

		if commit:
		 user.save()

		return user

class VolunteerForm(forms.ModelForm):
	class Meta:
		model = Volunteer
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'birth_date',
			'gender',
			'phone',
            'nationality',
			'current_city',
			'address',
			'password',
			'conform_password',
			)
	def save(self, commit=True):
		user = super(VolunteerForm, self).save()

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
			'travelling_From',
			'travelling_To',
			'arrival_city',
			'number_of_Adult_travellers',
			'number_of_Children_travellers',
			'arrival_date',
			'purpose',
			)

	def save(self, commit=True):
		user = super(BookNowForm, self).save()
		
		if commit:
		 user.save()

		return user