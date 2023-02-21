from django.shortcuts import render,redirect
from django.views.generic import View


# Create your views here.
class Homepage(View):
    def get(self,req,*args,**kwargs):
        return render(req,"Homepage.html")
    
class SignUp(View):
    def get(self,req,*args,**kwargs):
        return render(req,"SignUp.html")