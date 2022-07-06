from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages

def regi(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            # messages.add_message(request, messages.SUCCESS, "You are successfully registered!")
            messages.success(request, "You are successfully registered!")
        fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form':fm})
