# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class OpenIssues(models.Model):
    user = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    files = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    tags = models.CharField(max_length=50)

class ClosedIssues(models.Model):
    user = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    files = models.CharField(max_length=100)
    tags = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    explanation = models.CharField(max_length=50)

class ScriptCollection(models.Model):
    code = models.CharField(max_length=50)
    explanation = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    files = models.CharField(max_length=100)
    tags = models.CharField(max_length=50)
