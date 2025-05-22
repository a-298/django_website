from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import TimeForm


def home(request):
    if request.method == "POST":
        form = TimeForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            messages.success(request, "Your data was successfully recorded.")
    else:
        form = TimeForm()
    return render(request, "home.html", {"form": form})

