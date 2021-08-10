from typing import Reversible
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .forms import signUpForm , UserForm,ProfileForm
from .models import profile
from django.urls.base import reverse
from django.db.models.query import QuerySet


def signup(request):
    if request.method=="POST":
        form=signUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form=signUpForm()
    return render(request,'registration/signup.html',{'form':form})


def Profile(request):
    Profile=profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':Profile})

def profile_edit(request):
    Profile=profile.objects.get(user=request.user)

    if request.method=='POST':
        userform=UserForm(request.POST,instance=request.user)
        profileform=ProfileForm(request.POST,request.FILES,instance=Profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myProfileForm=profileform.save(commit=False)
            myProfileForm.user=request.user
            myProfileForm.save()
            return redirect(reverse('accounts:profile'))

    else:
        userform=UserForm(instance=request.user)
        profileform=ProfileForm(instance=Profile)
    return render(request,'accounts/edit_profile.html',{'userform':userform,'profileform':profileform})