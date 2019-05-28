# Make it clear which urls.py we are working in
"""Defines URL patterns for learning_logs."""

#Import the path function to map URLs to views
from django.urls import path

# Import views module
from . import views

# variable helps Django distinguish from other urls.py files
app_name = 'learning_logs'

# list of pages that can be requesed from learning_logs app
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]