from django import forms
from myuser.models import MyUser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

class CreateUserForm(forms.Form):
    display_name = forms.CharField(max_length=20)
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
