from django.contrib.auth.views import LoginView

# from django.contrib.auth.views import SignupView
from django.urls import path

from .views import SignupView

from . import views

urlpatterns = [
    path("login/", LoginView.as_view(template_name="auth/login.html"), name="login"),
    path("signup/", SignupView.as_view(), name="signup"),
]
