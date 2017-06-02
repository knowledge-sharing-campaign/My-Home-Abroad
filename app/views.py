# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'app/index.html', context)
def test(request):
	context = {}
	return render(request, 'app/test.html', context)
