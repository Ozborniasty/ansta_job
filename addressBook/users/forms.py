from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Osoba
from django import forms

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = Osoba
        fields = ['imie', 'nazwisko']

class UserForm(forms.ModelForm):
    class Meta:
        model = Osoba
        fields = ['imie', 'nazwisko']

