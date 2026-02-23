from django.urls import path
from . import views

app_name = "notifications"

urlpatterns = [
    path("mark-read/", views.mark_all_read, name="mark_all_read"),
]
