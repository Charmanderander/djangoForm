# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import RequestContext
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def open(request):
    my_data_dictionary = {}
    return render(request, 'index.html', my_data_dictionary)

def closed(request):
    return HttpResponse("You're at the closed page.")

def collection(request):
    return HttpResponse("You're at the collections page.")

def submit(request):
    return HttpResponse("You're at the submit page.")
