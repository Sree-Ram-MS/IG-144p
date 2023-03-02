from django.urls import path
from .views import UserHome,Profile,LogOut,BioAdd,BioEdit

urlpatterns = [
    path("userpage/",UserHome.as_view(),name="userpage"),
    path("profie/",Profile.as_view(),name="Profile"),
    path("logout/",LogOut.as_view(),name="Logout"),
    path("AddBio/",BioAdd.as_view(),name="AddBio"),
    path("EditBio/<int:pk>",BioEdit.as_view(),name="EditBio"),

] 

