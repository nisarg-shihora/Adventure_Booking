from django.forms import ModelForm
from django import forms
from .models import *

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    # number = forms.CharField(max_length=15)
    number = forms.CharField(max_length=10, min_length=10)
    message = forms.CharField(widget=forms.Textarea, min_length=10)
