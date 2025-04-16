from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('sign_up', views.players_signup, name='sign_up'),
    path('log_in', views.players_login, name='log_in'),
    path('', views.main_page, name='main_page'),
    path('log_out', views.players_logout, name='log_out'),
    path('user_profile', views.players_profile, name='user_profile'),
    path('about', views.about, name='about'),
    path('delete_account', views.delete_account, name='delete_account'),
    path('reset_password/', views.CustomPasswordResetView.as_view(template_name='reset_password_form.html'),
         name='password_reset'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password_done.html'),
         name='password_reset_done'),
    path('reset_password_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='reset_password_confirm.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'),
         name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
