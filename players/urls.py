from django.urls import path
from . import views

urlpatterns = [
    path('sign_up', views.players_signup, name='sign_up'),
    path('log_in', views.players_login, name='log_in'),
    path('', views.main_page, name='main_page'),
    path('log_out', views.players_logout, name='log_out'),
    path('user_profile', views.players_profile, name='user_profile'),
    path('about', views.about, name='about'),
]
