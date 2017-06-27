# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import RequestContext
from django.shortcuts import render
from .forms import NameForm
from django.http import HttpResponse
from .models import *
# Create your views here.

def open(request):
    #openIssues = OpenIssues(user='Jinhao', title='Test title', description='Test description', files='CSV', tags='tags and stuff')
    #openIssues.save()
    openIssues = OpenIssues.objects.all()
    my_data_dictionary = {'issues':openIssues}
    return render(request, 'open.html', my_data_dictionary)

def closed(request):
    my_data_dictionary = {}
    return render(request, 'closed.html', my_data_dictionary)

def collection(request):
    my_data_dictionary = {}
    return render(request, 'collection.html', my_data_dictionary)

def submit(request):
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'submit.html', {'form': form})
