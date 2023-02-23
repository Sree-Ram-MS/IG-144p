from django.urls import path
from .views import UserHome

urlpatterns = [
    path("userpage/",UserHome.as_view(),name="userpage")
]
