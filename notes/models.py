from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from course.models import Course
from tags.models import Tag

from ckeditor.fields import RichTextField


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, related_name="notes", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name="notes", blank=True)
    is_archived = models.BooleanField(default=False)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_by",
        "created_at",
        "modified_at",
        "is_archived",
        "is_private",
    )


class TextElement:
    pass


class FileElement:
    pass
