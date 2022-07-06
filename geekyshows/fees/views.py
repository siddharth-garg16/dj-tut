from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def fee_info(request):
    d = datetime.now()
    django_details = {'uname' : "Siddharth", "seats" : 50, "dt":d}
    return render(request, 'fees/fee.html', context = django_details)