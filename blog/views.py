from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .models import Post


def create_posts_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, "create_posts.html", {"form": form})


def latest_posts_view(request):
    posts = Post.objects.order_by("-date")[:5]
    return render(request, "latest_posts.html", {"posts": posts})


def specific_posts_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "specific_posts.html", {"post": post})
