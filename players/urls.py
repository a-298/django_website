from django.urls import path
from . import views

urlpatterns = [
    path('sign_up', views.player_registration, name='sign_up'),
    # path('sign-in', views.sign_in, name='sign_in'),
    # path('home', views.home, name='home'),
]