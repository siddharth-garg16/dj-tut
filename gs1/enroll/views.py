from django.shortcuts import render
# from django.http import HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student

def ShowStudentData(request):
    if request.method == "POST":
        sm = StudentRegistration(request.POST)
        if sm.is_valid():
            nm = sm.cleaned_data['name']
            mail = sm.cleaned_data['email']
            pswrd = sm.cleaned_data['password']
            # print(nm, mail, pswrd)
            reg = Student(name=nm, email=mail, password=pswrd)
            reg.save()
    else:
        sm = StudentRegistration()
    return render(request, 'enroll/studentform.html', {'form':sm})
