from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,FormView
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your views here.
# class Homepage(View):
#     def get(self,req,*args,**kwargs):
#         form =LoginForm()
#         return render(req,"Homepage.html",{"form":form})


class Homepage(FormView):
    template_name="Homepage.html"
    form_class=LoginForm
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
                return redirect("userpage")
            else:
                messages.error(req,"Login Failed")
                return redirect("Homepage")
        else:
            return render (req,"Homepage.html",{"form":form_data})

    
# class SignUp(View):
#     form_class=RegistrationForm
#     template_name="SignUp.html"
#     model=User
#     success_url=reverse_lazy("Homepage")
#     def get(self,req,*args,**kwargs):
#         form=self.form_class()
#         return render(req,self.template_name,{"form":form})
#     def post(self,req,*args,**kwargs):
#         form_data=self.form_class(data=req.POST)
#         if form_data.is_valid():
#             form_data.save()
#             messages.success(req,"User Registration Completed")
#             return redirect(self.success_url)
#         else:
#             return render(req,self.template_name,{"form":form_data})
        
class SignUp(CreateView):
    form_class=RegistrationForm
    template_name="SignUp.html"
    model=User
    success_url=reverse_lazy("Homepage")
        

   
    
