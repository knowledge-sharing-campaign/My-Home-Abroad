# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


class User(models.Model):
	firstname = models.CharField(max_length=15)
	lastname = models.CharField(max_length=15)
	email = models.CharField(max_length=25)
	nationality = models.CharField(max_length=40)
	phone = models.IntegerField()
	gender = models.CharField(max_length=7)
	age = models.IntegerField()

class Volunteer(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	email = models.CharField(max_length=25)
	birth_date = models.IntegerField()
	gender = models.CharField(max_length=25)
	phone = models.IntegerField()
	nationality = models.CharField(max_length=40)
	current_city = models.CharField(max_length=40)
	address = models.CharField(max_length=50)
	password = models.CharField(max_length=40)
	conform_password = models.CharField(max_length=40)


class BookNow(models.Model):
	first_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)
	gender = models.CharField(max_length=7)
	age = models.IntegerField()
	email = models.EmailField(max_length=25)
	nationality = models.CharField(max_length=40)
	travelling_From = models.CharField(max_length=40)
	travelling_To = models.CharField(max_length=40)
	arrival_city = models.CharField(max_length=50)
	number_of_Adult_travellers = models.IntegerField()
	number_of_Children_travellers = models.IntegerField()
	arrival_date = models.DateField()
	purpose = models.CharField(max_length=20)
