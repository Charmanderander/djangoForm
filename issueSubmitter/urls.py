from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^open/', views.open, name='open'),
    url(r'^closed/', views.closed, name='closed'),
    url(r'^collection/', views.collection, name='collection'),
    url(r'^submit/', views.submit, name='submit'),
    url(r'^$', views.open, name='open')
]
