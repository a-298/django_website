from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from .forms import PostForm
from .models import Post
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


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
    if request.user.is_authenticated:
        posts = Post.objects.filter(
            Q(is_posted=True) |
            Q(author=request.user, is_posted=False)
        ).distinct().order_by("-date")
    else:
        posts = Post.objects.filter(is_posted=True).order_by("-date")
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "latest_posts.html", {"posts": posts})


@require_http_methods(["GET", "POST"])
def specific_posts_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        if str(request.user) == post.author and not post.is_posted:
            post.is_posted = True
            post.save()
            return redirect("blog:specific_posts", post_id=post.id)
        else:
            post.is_posted = False
            post.save()
            return redirect("blog:specific_posts", post_id=post.id)
    if not post.is_posted:
        if not request.user.is_authenticated or str(request.user) != post.author:
            raise Http404("Post not found")
    return render(request, "specific_posts.html", {"post": post})


def edit_posts_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if str(request.user) != post.author:
        return redirect("blog:specific_posts", post_id=post.id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog:specific_posts", post_id=post_id)
    else:
        form = PostForm(instance=post)
    return render(request, "edit_posts.html", {"form": form})
