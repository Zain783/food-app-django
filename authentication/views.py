from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from .models import Profile


class SignupView(View):
    template_name = "auth/register.html"
    profile_form_class = Profile

    def get(self, request):
        form = self.form_class()
        profile_form = self.profile_form_class()
        return render(
            request, self.template_name, {"form": form, "profile_form": profile_form}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        profile_form = self.profile_form_class(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            user_profile = profile_form.save(commit=False)
            user_profile.user = user
            user_profile.save()
            login(request, user)
            return redirect("home")
        return render(
            request, self.template_name, {"form": form, "profile_form": profile_form}
        )


class LoginView(View):
    template_name = "auth/login.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, self.template_name)
