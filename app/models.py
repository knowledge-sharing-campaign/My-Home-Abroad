# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	firstname = models.CharField(max_length=15)
	lastname = models.CharField(max_length=15)
	email = models.CharField(max_length=25)
	nationality = models.CharField(max_length=40)
	phone = models.IntegerField()
	gender = models.CharField(max_length=7)
	DOB = models.IntegerField()

