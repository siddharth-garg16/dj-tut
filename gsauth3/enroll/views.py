from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, AuthenticationForm, SetPasswordForm
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


def sign_up(request):
    if request.method=="POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, "Account created successfully!")
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'enroll/signup.html', {'form':fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in successfully.")
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/userlogin.html', {'form':fm})
    else:
        HttpResponseRedirect('/profile/')


def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/profile.html', {'name':request.user})
    return HttpResponseRedirect("/login/")

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

#change password with old password
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm = PasswordChangeForm(user = request.user, data= request.POST)
            if fm.is_valid():
                fm.save()
                # logout(request)
                # return HttpResponseRedirect('/login/')
                update_session_auth_hash(request, fm.user)
                messages.success(request, "Password changed successfully!")
                return HttpResponseRedirect('/profile/')

        else:
            fm = PasswordChangeForm(user = request.user)
        return render(request, 'enroll/changepass.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')

#change password without old password
def user_change_pass1(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm = SetPasswordForm(user = request.user, data= request.POST)
            if fm.is_valid():
                fm.save()
                # logout(request)
                # return HttpResponseRedirect('/login/')
                update_session_auth_hash(request, fm.user)
                messages.success(request, "Password changed successfully!")
                return HttpResponseRedirect('/profile/')

        else:
            fm = SetPasswordForm(user = request.user)
        return render(request, 'enroll/changepass1.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')


