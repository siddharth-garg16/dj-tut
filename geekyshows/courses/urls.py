from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('learn-django', views.learn_dj, name='available_courses'),
]