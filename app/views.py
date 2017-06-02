# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'app/index.html', context)
def login(request):
	context = {}
	return render(request, 'app/login.html', context)
def logout(request):
	context = {}
	return render(request, 'app/logout.html', context)
def policies(request):
	context = {}
	return render(request, 'app/policies.html', context)
def refer(request):
	context = {}
	return render(request, 'app/refer.html', context)
def schedule(request):
	context = {}
	return render(request, 'app/schedule.html', context)
def volunteer(request):
	context = {}
	return render(request, 'app/volunteer.html', context)