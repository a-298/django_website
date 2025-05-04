from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("create_posts/", views.create_posts_view, name="create_posts"),
    path("latest_posts/", views.latest_posts_view, name="latest_posts"),
    path("latest_posts/<int:post_id>/", views.specific_posts_view, name="specific_posts"),
    path("latest_posts/<int:post_id>/edit", views.edit_posts_view, name="edit_posts"),
]
