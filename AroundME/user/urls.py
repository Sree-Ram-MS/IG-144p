from django.urls import path
from .views import UserHome,Profile,LogOut,BioEdit
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("userpage/",UserHome.as_view(),name="userpage"),
    path("profie/",Profile.as_view(),name="Profile"),
    path("logout/",LogOut.as_view(),name="Logout"),
    path("EditBio/",BioEdit.as_view(),name="BioEdit"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

