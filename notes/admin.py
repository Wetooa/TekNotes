from django.contrib import admin
from .models import Note, NoteAdmin

admin.site.register(Note, NoteAdmin)