# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from app.forms import RegistrationForm 

def index(request):
    context = {}
    return render(request, 'index.html', context)

def home(request):
    context = {}
    return render(request, 'home.html', context)

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
	return render(request, 'volunteer.html', context)

def bookNow(request):
	context = {}
	return render(request, 'bookNow.html', context)

def traveller_reg(request):
	context = {}
	return render(request, 'traveller_reg.html', context)

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():	
			form.save()
			return redirect('/home')
	else:
		form = RegistrationForm()

		args = {'form': form}
		return render(request, 'register.html', args)


