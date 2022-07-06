from django.shortcuts import render
# from django.http import HttpResponseRedirect
from enroll.forms import StudentRegistration
from .models import Student

# def thankyou(request):
    # return render(request, 'enroll/success.html')

# Create your views here.
def ShowStudentData(request):
    if request.method == "POST":
        sm = StudentRegistration(request.POST)
        if sm.is_valid():
            # print('Validated Form')
            # print('Name:', sm.cleaned_data['name'])
            # print('Email:', sm.cleaned_data['email'])
            # print('Passowrd', sm.cleaned_data['password'])
            # return HttpResponseRedirect('/reg/success')
            nm = sm.cleaned_data['name']
            mail = sm.cleaned_data['email']
            pswrd = sm.cleaned_data['password']
            reg = Student(name = nm, email = mail, password = pswrd)
            reg.save()
    else:
        sm = StudentRegistration()
    return render(request, 'enroll/studentform.html', {'form':sm})
