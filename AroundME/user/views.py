from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,UpdateView,FormView,DeleteView
from django.contrib.auth import logout,authenticate
from django.contrib.auth.views import PasswordChangeView
from .forms import BioForm,CPForm,PostForm,CommentForm
from .models import Bio,Posts,Comments
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
        context['cform']=CommentForm()
        context["comments"]=Comments.objects.all()
        return context
def addcomment(request,*args,**kwargs):
    if request.method=="POST":
        cid=kwargs.get("cid")
        post=Posts.objects.get(id=cid)
        user=request.user
        cmnt=request.POST.get("comment")
        Comments.objects.create(comment=cmnt,user=user,post=post)
        return redirect ("userpage")

class PostEdit(UpdateView):
    form_class=PostForm
    model=Posts
    template_name="EditPost.html"
    success_url=reverse_lazy("Profile")
    pk_url_kwarg="pk"

class PostDelete(DeleteView):
    model=Posts
    template_name="DeletePost.html"
    success_url=reverse_lazy("Profile")

    

class Profile(TemplateView):
    template_name="UserProfile.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Posts.objects.filter(user=self.request.user).order_by('-datetime')
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
        
def addlike(req,*args, **kwargs):
    pid=kwargs.get("pid")
    post=Posts.objects.get(id=pid)
    user=req.user
    post.likes.add(user)
    post.save()
    return redirect ("userpage")

# class ChangePasswordView(PasswordChangeView):
#     template_name = 'change pswd.html's
#     success_url = reverse_lazy('profile')    