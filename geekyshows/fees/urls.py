from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('fee-information', views.fee_info, name='course_fees'),
]