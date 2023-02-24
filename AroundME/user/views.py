from django.shortcuts import render
from django.views.generic import View,TemplateView,CreateView

# Create your views here.
class UserHome(TemplateView):
    template_name="Userpage.html"

class Profile(TemplateView):
    template_name="UserProfile.html"