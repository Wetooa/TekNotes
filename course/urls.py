from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path("add_a_course/", views.add_a_course, name="add_a_course"),
]