from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'authentication'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<int:user_id>/notes/', views.profile, name='profile'),
    path('profile/<int:user_id>/likes/', views.profile_likes, name='profile_likes'),
    path('profile/<int:user_id>/courses/', views.profile_courses, name='profile_courses'),
]