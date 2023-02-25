from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView
from django.contrib.auth import logout

# Create your views here.
class UserHome(TemplateView):
    template_name="Userpage.html"

class Profile(TemplateView):
    template_name="UserProfile.html"

class LogOut(View):
    def get(self,req):
        logout(req)
        return redirect("Homepage")