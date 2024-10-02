from django.urls import path
from authentication import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('register_user/', views.register_user, name='Register'),
    path('login_user/', views.login_user, name='Login'),
    path('logout_user/', views.logout_user, name='Logout')
]