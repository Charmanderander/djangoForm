# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import RequestContext
from django.shortcuts import render
from .forms import NameForm
from django.http import HttpResponseRedirect
from .models import *
# Create your views here.

def open(request):
    #openIssues = OpenIssues(user='Jinhao', title='Test title', description='Test description', files='CSV', tags='tags and stuff')
    #openIssues.save()
    openIssues = OpenIssues.objects.all()
    my_data_dictionary = {'openIssues':openIssues}
    return render(request, 'open.html', my_data_dictionary)

def closed(request):
    closedIssues = ClosedIssues.objects.all()
    my_data_dictionary = {'closedIssues':closedIssues}
    return render(request, 'closed.html', my_data_dictionary)

def collection(request):
    collection = ScriptCollection.objects.all()
    my_data_dictionary = {'collection':collection}
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
            print "writing to db..."
            openIssues = OpenIssues(user='testUser', title=form.cleaned_data['title'], description=form.cleaned_data['description'], files=form.cleaned_data['files'], tags=form.cleaned_data['tags'])
            openIssues.save()
            return HttpResponseRedirect('/open')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'submit.html', {'form': form})
