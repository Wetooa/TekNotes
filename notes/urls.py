from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path("tek_a_note/", views.tek_a_note, name="tek_a_note"),
    path('delete_note/<int:note_id>/', views.delete_note, name="delete_note"),
    path("hide_note/<int:note_id>/", views.hide_note, name="hide_note"),
    path("archive_note/<int:note_id>/", views.archive_note, name="archive_note"),
    path('<int:note_id>/', views.note_detail, name="note_detail"),
]