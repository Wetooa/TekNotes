from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("notebook/", views.notebook, name="notebook"),
    path("likes/", views.likes, name="likes"),
    path("archive/", views.archive, name="archive"),
]

