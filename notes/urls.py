from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    path("tek_a_note/", views.tek_a_note, name="tek_a_note"),
    path("<int:note_id>/delete/", views.delete_note, name="delete_note"),
    path("<int:note_id>/edit/", views.edit_note, name="edit_note"),
    path("<int:note_id>/hide/", views.hide_note, name="hide_note"),
    path("<int:note_id>/archive/", views.archive_note, name="archive_note"),
    path("<int:note_id>/", views.note_detail, name="note_detail"),
]
