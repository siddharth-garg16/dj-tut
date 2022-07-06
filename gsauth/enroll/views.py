from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages

def sign_up(request):
    if request.method=="POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, "Account created successfully!")
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'enroll/signup.html', {'form':fm})
