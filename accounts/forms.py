from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import profile

class signUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=profile
        fields=['nationalID','collageID','phoneNumber','city','image']