from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def sign_up(request):
    pass


def sign_in(request):
    pass
