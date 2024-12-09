from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path("add_a_course/", views.add_a_course, name="add_a_course"),
    path("<int:course_id>/delete/", views.delete_course, name="delete_course"),
    path("<int:course_id>/edit/", views.edit_course, name="edit_course"),
]