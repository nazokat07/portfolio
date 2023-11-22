from django.urls import path
from .views import *

urlpatterns = [
  path('', index, name='index'),
  path('templates/about.html', about, name='about'),
  path('templates/admin.html', admin, name='admin'),
  path('templates/contact.html', contact, name='contact'),
  path('templates/projects.html', projects, name='projects'),
  path('templates/home.html', home, name='home'),
  ]

