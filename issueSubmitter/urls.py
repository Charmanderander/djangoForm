from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [

    url(r'^open/', views.open, name='open'),
    url(r'^closed/', views.closed, name='closed'),
    url(r'^collection/', views.collection, name='collection'),
    url(r'^submit/', views.submit, name='submit'),
    url(r'^.*$', RedirectView.as_view(pattern_name='open', permanent=False))
]
