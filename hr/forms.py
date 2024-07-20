from django import forms
from app.models import Category,job

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class categoryform(forms.ModelForm):
    class Meta:
        model=Category
        fields=["Name"]

class jobform(forms.ModelForm):
    class Meta:
        model=job
        #exclude=(fieldname,)
        fields='__all__'