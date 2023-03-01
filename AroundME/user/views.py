from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView
from django.contrib.auth import logout
from .forms import BioForm
from .models import Bio
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
class UserHome(TemplateView):
    template_name="Userpage.html"

class Profile(TemplateView):
    template_name="UserProfile.html"

class LogOut(View):
    def get(self,req):
        logout(req)
        return redirect("Homepage")
    
class BioAdd(CreateView):
    form_class=BioForm
    template_name="Bio.html"
    model=Bio
    success_url=reverse_lazy("Profile")
    def form_valid(self,form):
        form.instance.user=self.request.user
        self.object = form.save()
        messages.success(self.request,"Bio Updated")
        return super().form_valid(form)


class BioEdit(View):
    def get(self,req,*args,**kwargs,id):
        Bioid=Bio.objects.get(id=id)
        form=BioForm(instance=Bioid)
        return render(req,"BioEdit.html",{"form":form})
    def post(self,req,*args,**kwargs):
        id=kwargs.get("sid")
        Bio=Bio.objects.get(id=id)
        form_data=BioForm(data=req.POST,files=req.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(req,"Bio Details Updated")
            return redirect ('Profile')
        else:
            messages.success(req,"Bio Details Updation failed")
            return render (req,"BioEdit.html",{"form":form_data})