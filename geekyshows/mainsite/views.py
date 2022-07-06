from django.shortcuts import render

def home(request):
    return render(request, "mainsite/homepage.html")