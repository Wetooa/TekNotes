from django.urls import include, path
import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
]
