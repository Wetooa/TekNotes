from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tek-a-note", views.tek_a_note, name="tek-a-note"),
]
