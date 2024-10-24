from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path("add_a_course/", views.add_a_course, name="add_a_course"),
    path("delete_course/<int:course_id>/", views.delete_course, name="delete_course"),
]