from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def player_registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form.add_error(None, "Invalid username or password.")
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', {"form": form})
