from django.urls import path
from . import views

urlpatterns = [
    path('sign_up', views.players_signup, name='sign_up'),
    path('log_in', views.players_login, name='log_in'),
    path('main_page', views.main_page, name='main_page'),
]