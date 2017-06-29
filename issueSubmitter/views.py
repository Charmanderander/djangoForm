# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import RequestContext
from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
from .models import *
# Create your views here.

def solve(request):
    issueID = request.GET.get("id", False)
    issue = OpenIssues.objects.filter(id=issueID)

    if 'id' not in request.session:
         request.session['id'] = issueID

    if request.method == 'POST' and issueID==False:
        # create a form instance and populate it with data from the request:
        form = SolveForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print "writing to db..."

            issue = OpenIssues.objects.filter(id=request.session['id'])

            closedIssues = ClosedIssues(user=issue[0].user, title=issue[0].title, \
                 description=issue[0].description, files=issue[0].files, tags=issue[0].tags, \
                 code=form.cleaned_data['code'], explanation=form.cleaned_data['explanation'])

            closedIssues.save()
            issue.delete()
            return HttpResponseRedirect('/closed')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SolveForm()

    my_data_dictionary = {'form':form,'issue':issue[0],'admin': True}
    return render(request, 'solve.html', my_data_dictionary)

def adminView(request):
    openIssues = OpenIssues.objects.all()
    my_data_dictionary = {'openIssues':openIssues,'admin': True}
    return render(request, 'open.html', my_data_dictionary)

def open(request):
    openIssues = OpenIssues.objects.all()
    my_data_dictionary = {'openIssues':openIssues, 'admin': False}
    return render(request, 'open.html', my_data_dictionary)

def closed(request):
    closedIssues = ClosedIssues.objects.all()
    my_data_dictionary = {'closedIssues':closedIssues, 'admin': False}
    return render(request, 'closed.html', my_data_dictionary)

def collection(request):
    collection = ScriptCollection.objects.all()
    my_data_dictionary = {'collection':collection, 'admin': False}
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
    my_data_dictionary = {'form': form, 'admin': 'no'}
    return render(request, 'submit.html', my_data_dictionary)
