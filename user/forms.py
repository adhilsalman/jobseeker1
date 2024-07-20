from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm # password verification
from app.models import student

class Registration(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

#class Loginform(forms.Form):
    #username=forms.CharField()
    #password=forms.CharField()

class Studentprofile(forms.ModelForm):
    class Meta:
        model=student
        exclude=('user',)
        fields="__all__"

