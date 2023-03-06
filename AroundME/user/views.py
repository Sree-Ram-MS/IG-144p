from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,UpdateView,FormView
from django.contrib.auth import logout,authenticate
from .forms import BioForm,CPForm,PostForm,UserPostForm
from .models import Bio,Posts
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
class UserHome(CreateView):
    template_name="Userpage.html"
    form_class=PostForm
    model=Posts
    success_url=reverse_lazy("userpage")
    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,'Post Uploaded')
        self.object=form.save()
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Posts.objects.all().order_by('-datetime')
        # user=req.user
        return context

class Profile(CreateView):
    template_name="UserProfile.html"
    form_class=UserPostForm
    model=Posts
    success_url=reverse_lazy("profile")
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        id=self.request.user
        context["data"]=Posts.objects.filter(id).order_by('-datetime')
        return context

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


class BioEdit(UpdateView):
    form_class=BioForm
    model=Bio
    template_name="EditBio.html"
    success_url=reverse_lazy("Profile")
    pk_url_kwarg="pk"

class ChangePassword(FormView):
    form_class=CPForm
    template_name="ChangePassword.html"
    def post(self,req,*args, **kwargs):
        form_data=CPForm(data=req.POST)
        if form_data.is_valid():
            current=form_data.cleaned_data.get("cp")
            new=form_data.cleaned_data.get("np")
            confirm=form_data.cleaned_data.get("cnp")
            print(current)
            user=authenticate(req,username=req.user.username,password=current)
            if user:
                if new==confirm:
                    user.set_password(new)
                    user.save()
                    messages.success(req,"Password Changed")
                    logout(req)
                    return redirect('Homepage')
                else:
                    messages.error(req,"Password  mismatched")
                    return redirect("CPass")
            else:
                messages.error(req,"Incorrect Password")
                return redirect("CPass")
        else:
            return render(req,"ChangePassword.html",{"form":form_data})

