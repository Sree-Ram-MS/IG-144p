from django.urls import path
from .views import UserHome,Profile,LogOut,BioAdd,BioEdit,ChangePassword,PostEdit,PostDelete,addcomment,addlike

urlpatterns = [
    path("userpage/",UserHome.as_view(),name="userpage"),
    path("profie/",Profile.as_view(),name="Profile"),
    path("logout/",LogOut.as_view(),name="Logout"),
    path("AddBio/",BioAdd.as_view(),name="AddBio"),
    path("EditBio/<int:pk>",BioEdit.as_view(),name="EditBio"),
    path("EditPost/<int:pk>",PostEdit.as_view(),name="EditPost"),
    path("DelPost/<int:pk>",PostDelete.as_view(),name="DelPost"),
    path("ChangePAssword",ChangePassword.as_view(),name="CPass"),
    path("Commetn/<int:cid>",addcomment,name="cmnt"),
    path("liked/<int:pid>",addlike,name="like"),

] 

