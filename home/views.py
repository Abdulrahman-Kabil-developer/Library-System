from typing import Reversible
from django.shortcuts import redirect, render


def homePage(request):
    return render(request,'home/home.html',{})
# Create your views here.
