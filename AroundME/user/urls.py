from django.urls import path
from .views import UserHome,Profile

urlpatterns = [
    path("userpage/",UserHome.as_view(),name="userpage"),
    path("profie/",Profile.as_view(),name="Profile")
]
