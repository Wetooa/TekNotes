from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import Q
from course.models import Course
from notes.models import Note
from tags.models import Tag

def search(request):
    query = request.GET.get('query', '')
    if not query:
        return HttpResponseRedirect('/')
    notes = Note.objects.filter(
        Q(title__icontains=query) | 
        Q(created_by__username__icontains=query) |
        Q(created_by__first_name__icontains=query) |
        Q(created_by__last_name__icontains=query) |
        Q(tags__name__icontains=query) |
        Q(course__code__icontains=query) |
        Q(course__description__icontains=query) |
        Q(content__icontains=query),
        is_archived=False,
        is_private=False
    ).distinct()
    tags = Tag.objects.filter(notes__in=notes).distinct()
    courses = Course.objects.filter(Q(code__icontains=query) | Q(description__icontains=query)).distinct()
    users = User.objects.filter(Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(profile__bio__icontains=query) | Q(email__icontains=query)).distinct()

    return render(request, 'advanced_search/search_results.html', {
        'notes': notes,
        'tags': tags,
        'query': query,
        'title': 'Search results for: ' + (query[:8] + '...' if len(query) > 8 else query),
        'courses': courses,
        'users': users,
    })