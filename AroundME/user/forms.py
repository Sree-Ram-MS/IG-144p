from django import forms
from .models import Bio,Posts,Comments

class BioForm(forms.ModelForm):
    class Meta:
        model=Bio
        exclude=["user"]
        widgets={
            "dob":forms.DateInput(attrs={"type":"date","class":"form-control form-control-lg"}),
            "gender":forms.Select(attrs={"class":"form-control"}),
            "phone":forms.NumberInput(attrs={"class":"form-control form-control-lg"}),
            "status":forms.TextInput(attrs={"class":"form-control"}),
        }

class CPForm(forms.Form):
    cp=forms.CharField(max_length=100,label="Current Password",widget=forms.PasswordInput)
    np=forms.CharField(max_length=100,label="New Password",widget=forms.PasswordInput)
    cnp=forms.CharField(max_length=100,label="Confirm Password",widget=forms.PasswordInput)

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["Image","caption"]
        widgets={
            "Image":forms.FileInput(),
            "caption":forms.TextInput(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields =["comment"]
        widgets={
            "comment":forms.Textarea(attrs={"class":"form-control"}),
        }
