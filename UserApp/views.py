from django.shortcuts import render
from .forms import ContactForm
from .models import Form
from django.contrib import messages


def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            birth_date = form.cleaned_data["birth_date"]

            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, birth_date=birth_date)
            messages.success(request, "Signed up successfully!")
    return render(request, "index.html")
