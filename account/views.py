from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from .forms import LoginForm,SigninForm,UserEditeForm

def s_profile(request):
    return render(request,"account/profile.html",{})
def s_login(request):
    if request.user.is_authenticated == True :
        return redirect("home_app:index")
    if request.method == 'POST':
      form = LoginForm(request.POST)
      if form.is_valid():
          user = User.objects.get(username=form.cleaned_data.get('username'))
          login(request,user)
          return redirect('home_app:index')
    else:
        form = LoginForm()
    return render(request,  'account/login.html', {"form": form})
def s_logout (request):
    logout(request)
    return redirect("home_app:index")


def s_signin(request):
    if request.user.is_authenticated == True :
        return redirect("home_app:index")
    if request.method == 'POST':
       us = SigninForm(request.POST)
       if us.is_valid():
            User.objects.create(username= us.cleaned_data.get('username'),password=us.cleaned_data.get('password'),first_name=us.cleaned_data.get('first_name'),last_name=us.cleaned_data.get('last_name'),email=us.cleaned_data.get('email'))
            return redirect("home_app:index")
    return render(request, 'account/signin.html', {"user":None})



def edit_user(request):
    user = request.user
    form = UserEditeForm(instance=user)
    if request.method == 'POST':
        form =UserEditeForm(instance=user,data=request.POST)
        if form.is_valid():
            form.save()
            return render(request,'account/edit_profile.html',{'form':form})
