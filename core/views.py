from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import OuterRef, Subquery
from notes.models import Note
from course.models import Course
from tags.models import Tag
from comments.models import Like

def index(request):
    notes = Note.objects.filter(is_archived=False, is_private=False).order_by('-modified_at')
    courses = Course.objects.filter(note__in=notes).distinct()
    tags = Tag.objects.filter(notes__in=notes).distinct()

    return render(request, 'core/index.html', {
        'notes': notes,
        'courses': courses,
        'tags': tags
    })

