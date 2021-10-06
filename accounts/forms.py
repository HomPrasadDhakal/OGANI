from django.contrib.auth.forms import UserCreationForm
from accounts.models import user
from django import forms
from accounts.validators import *
from django.core import validators

#FROMS FOR USER REGISTRATION
class CustomerRegistrationform(UserCreationForm):
    email =forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'enter your email',
    }))

    first_name =forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'enter your first name',
    }))

    last_name =forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'enter your last name',
    }))

    password1 =forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Choose your password',
    }))

    password2 =forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Confirm your password',
    }))

    class Meta:
        model = user
        fields = ['first_name','last_name','email','password1','password2']
