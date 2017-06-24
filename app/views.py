# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponseRedirect

from django.http import HttpResponse

from app.forms import RegisterForm

from app.forms import VolunteerForm
from .models import Volunteer


from django.contrib.auth.models import User

from app.forms import BookNowForm

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
def profile(request):
	context = {}
	return render(request, 'volunteer_profile.html', context)

def bookNow(request):
	context = {}
	return render(request, 'bookNow.html', context)

def traveller_reg(request):
	context = {}
	return render(request, 'traveller_reg.html', context)

def register(request):
    user_list = User.objects.all()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_obj = form.save()
            user_obj.save()

            return render(request, 'profile.html', {"first_name":request.POST.get('first_name'), "last_name":request.POST.get('last_name'),
															  "email":request.POST.get('email'), "birth_date":request.POST.get('birth_date'),
															  "gender":request.POST.get('gender'),"phone":request.POST.get('phone'),"nationality":request.POST.get('nationality'),
															  "username": request.POST.get('username')}
						  )
        else:
        	return HttpResponseRedirect("/register")
    else:
        form = VolunteerForm()
    	return render(request, 'register.html', {
        'form': form, 'user_list': user_list
        })


def volunteer(request):
    user_list = Volunteer.objects.all()
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            user_obj = form.save()
            user_obj.save()

            return render(request, 'volunteer_profile.html', {"first_name":request.POST.get('first_name'), "last_name":request.POST.get('last_name'),
															  "email":request.POST.get('email'), "birth_date":request.POST.get('birth_date'),
															  "gender":request.POST.get('gender'),"phone":request.POST.get('phone'),"nationality":request.POST.get('nationality'),
															  "current_city":request.POST.get('current_city'),"current_country":request.POST.get('current_country'),"address":request.POST.get('address'),
															  "username": request.POST.get('username')}
						  )
        else:
        	return HttpResponseRedirect("/volunteer")
    else:
        form = VolunteerForm()
    	return render(request, 'volunteer.html', {
        'form': form, 'user_list': user_list
        })


def bookNow(request):
    user_list = User.objects.all()
    if request.method == 'POST':
        form = BookNowForm(request.POST)
        if form.is_valid():
            user_obj = form.save()
            user_obj.save()

            return HttpResponseRedirect('/schedule')
        else:
        	return HttpResponse("Failed")
    else:
        form = BookNowForm()
    	return render(request, 'bookNow.html', {
        'form': form, 'user_list': user_list
        })

def about(request):
	context = {}
	return render(request, 'about_us.html', context)

def forgetting_passwd(request):
    context = {}
    return render(request, 'forgetting_passwd.html', context)
def my_schedul(request):
    context = {}
    return render(request, 'my_schedul.html', context)
