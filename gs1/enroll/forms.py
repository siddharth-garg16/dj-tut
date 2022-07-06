from tkinter import Widget
from django import forms
from django.core import validators
from .models import Student

class StudentRegistration(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']
        labels = {'name':'Enter Your Name', 'email':'Email Address', 'password':'Enter You Password'}
        error_messages = {'name':{'required':'It is a mandatory field.'},
                        'email':{'required':'It is a mandatory field.'},
                        'password':{'required':'It is a mandatory field.'}}

        widgets = {'name':forms.TextInput(attrs={'placeholder':'Username'}),
        'password':forms.PasswordInput(attrs={'placeholder':'Password'})}
