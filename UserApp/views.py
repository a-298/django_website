from django.shortcuts import render, redirect
from .forms import ContactForm, SignInForm
from .models import Form
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            birth_date = form.cleaned_data["birth_date"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = User(username=username)
            user.set_password(password)  # This hashes the password
            user.save()

            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, birth_date=birth_date, username=user.username,
                                password=user.password)
            messages.success(request, "Signed up successfully!")
    return render(request, "index.html")


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = SignInForm()
    return render(request, 'log_in.html', {"form": form})


def home(request):
    return render(request, 'main_page.html')

