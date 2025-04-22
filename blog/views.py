from django.shortcuts import render
from .forms import PostForm


def create_posts_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, "create_posts.html", {"form": form})


def all_posts_view(request):
    return render(request, "all_posts.html")
