from django.urls import path
from .views import (
    index,
    registration,
    projects
)

urlpatterns = [
    path('index.html', index, name='index'),
    path('', registration, name='registration'),
    path('projects.html', projects, name='projects')
]

