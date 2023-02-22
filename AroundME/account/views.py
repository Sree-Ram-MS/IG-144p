from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
class Homepage(View):
    def get(self,req,*args,**kwargs):
        form =LoginForm()
        return render(req,"Homepage.html",{"form":form})
    def post (self,req,*args,**kwargs):
        form_data=LoginForm(data=req.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("username")
            psw=form_data.cleaned_data.get("password")
            user=authenticate(req,username=un,password=psw)
            if user:
                print(user.first_name,user.last_name)
                login(req,user)
                messages.success(req,"LOgin SucCess")
                return redirect("SignUp")
            else:
                messages.error(req,"Login Failed")
                return redirect("Homepage")
        else:
            return render (req,"Homepage.html",{"form":form_data})
    
class SignUp(View):
    def get(self,req,*args,**kwargs):
        form=RegistrationForm()
        return render(req,"SignUp.html",{"form":form})
    def post(self,req,*args,**kwargs):
        form_data=RegistrationForm(data=req.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(req,"User Registration Completed")
            return redirect('Homepage')
        else:
            return render(req,"SignUp.html",{"form":form_data})
        

   
    
