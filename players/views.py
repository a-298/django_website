from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm


def players_signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form.add_error(None, "Invalid username or password.")
    else:
        form = CustomUserCreationForm()
    return render(request, "sign_up.html", {"form": form})


def players_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("main_page")
    else:
        form = AuthenticationForm()
    return render(request, "log_in.html", {"form": form})


def main_page(request):
    return render(request, "main_page.html")
