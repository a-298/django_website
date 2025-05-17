from django.urls import path
from . import views

app_name = "time_management"

urlpatterns = [
    path("home/", views.home, name="home"),
]