from django.urls import path
from .views import *

urlpatterns = [
    path("Reg/",SignUp.as_view(),name="SignUp")
]
