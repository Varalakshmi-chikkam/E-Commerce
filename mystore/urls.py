from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("signup/signup", views.signup, name="signup"),
]
