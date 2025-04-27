from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def create_posts_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            author = form.cleaned_data["author"]
            category = form.cleaned_data["category"]
            post = form.cleaned_data["post"]
            exists = Post.objects.filter(
                title=title,
                author=author,
                category=category,
                post=post
            ).exists()
            if exists:
                messages.warning(request, "A post with the same title, author, category, and content already exists.")
                return render(request, "create_posts.html", {"form": form})
            form.save()
            messages.success(request, "Post created successfully!")
            return redirect("blog:latest_posts")
    else:
        form = PostForm(user=request.user)
    return render(request, "create_posts.html", {"form": form})


def latest_posts_view(request):
    posts = Post.objects.order_by("-date")
    paginator = Paginator(posts, 5)

    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "latest_posts.html", {"posts": posts})


def specific_posts_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "specific_posts.html", {"post": post})
