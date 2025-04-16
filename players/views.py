from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.http import HttpResponseForbidden
from .forms import ProfileUpdateForm


class CustomPasswordResetView(PasswordResetView):
    def get_initial(self):
        initial = super().get_initial()
        if self.request.user.is_authenticated:
            initial['email'] = self.request.user.email
        return initial


def players_signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("log_in")
    else:
        form = CustomUserCreationForm()
    return render(request, "sign_up.html", {"form": form})


def players_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("user_profile")

    else:
        form = AuthenticationForm()
    return render(request, "log_in.html", {"form": form})


def main_page(request):
    return render(request, "main_page.html")


def players_logout(request):
    logout(request)
    return redirect("main_page")


def players_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, "user_profile.html", {
        "user": request.user,
        "form": form,
    })


def about(request):
    return render(request, "about.html")


def delete_account(request):
    if request.method == "GET":
        return render(request, "delete_account.html")
    elif request.method == "POST":
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, "Your account has been successfully deleted.")
        return redirect("main_page")
    return HttpResponseForbidden()
