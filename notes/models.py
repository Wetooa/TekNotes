from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from course.models import Course
from tags.models import Tag


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = CKEditor5Field("Text", config_name="extends", blank=True, null=True)
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

    def __str__(self):
        return self.title


class Click(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.note.title + " clicked at " + str(self.created_at)
