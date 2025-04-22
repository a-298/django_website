from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("create_post/", views.create_posts_view, name="create_posts"),
    path("posts_list/", views.all_posts_view, name="all_posts"),
]
