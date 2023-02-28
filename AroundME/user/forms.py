from django import forms
from .models import Bio

class BioForm(forms.ModelForm):
    class Meta:
        model=Bio
        exclude=["user"]
        widgets={
            "dob":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "gender":forms.Select(attrs={"class":"form-control"}),
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
        }