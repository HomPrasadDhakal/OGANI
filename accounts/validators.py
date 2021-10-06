from django.core import validators
from django import forms




def non_empty_value(value):
    if not value():
        raise forms.validationError("Please fill the field ! ")
    return value