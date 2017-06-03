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
	return render(request, 'volunteer.html', context)

def BookNow(request):
	context = {}
	return render(request, 'BookNow.html', context)
def register(request):
	context = {}
	return render(request, 'register.html', context)

# def test(request):
#       if request.method == 'POST':
#           form = CreateAccountForm(request.POST)
#           if form.is_valid():
#               return HttpResponse('OK')
#       else:
#             return HttpResponse(json.dumps(form.errors))