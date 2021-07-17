from django import forms
from django.db.models import fields
from .models import book

class bookForm(forms.ModelForm):
    class Meta:
        model=book
        fields='__all__'
        exclude=('owner','slug',)