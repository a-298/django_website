from django.urls import path
from . import views

app_name = "time_management"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("home/<str:timeframe>/", views.home, name="home"),
]