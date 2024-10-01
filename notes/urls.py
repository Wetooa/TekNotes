from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("your-notes", views.tek_a_note, name="your-notes"),
    path("likes", views.tek_a_note, name="likes"),
    path("tek-a-note", views.tek_a_note, name="tek-a-note"),
]
