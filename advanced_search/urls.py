from django.urls import path
from . import views

app_name = "advanced_search"

urlpatterns = [
    path("", views.search, name="search"),
    path("course_<int:course_id>/", views.view_course, name="view_course"),
]
