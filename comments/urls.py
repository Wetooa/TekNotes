from django.urls import path
from . import views

app_name = "comments"

urlpatterns = [
    path("comment/<int:note_id>/", views.comment, name="comment"),
    path("like/<int:note_id>/", views.like, name="like"),
    path("dislike/<int:note_id>/", views.dislike, name="dislike"),
]
