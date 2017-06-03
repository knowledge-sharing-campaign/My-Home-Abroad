# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'index.html', context)
def login(request):
	context = {}
	return render(request, 'login.html', context)
def logout(request):
	context = {}
	return render(request, 'logout.html', context)
def policies(request):
	context = {}
	return render(request, 'policies.html', context)
def refer(request):
	context = {}
	return render(request, 'refer.html', context)
def schedule(request):
	context = {}
	return render(request, 'schedule.html', context)
def volunteer(request):
	context = {}
<<<<<<< HEAD
	return render(request, 'app/volunteer.html', context)

def BookNow(request):
	context = {}
	return render(request, 'app/BookNow.html', context)
=======
	return render(request, 'volunteer.html', context)
>>>>>>> 7b2df28df5ca7299bfecdfbe8a8db2903c6cba39
