from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_dj(request):
    return HttpResponse('<h1>Django and Python courses available!</h1>')