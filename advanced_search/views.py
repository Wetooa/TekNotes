from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import Q
from course.models import Course
from notes.models import Note
from tags.models import Tag


def search(request):
    query = request.GET.get('query', '').strip()
    category = request.GET.get('category', '').strip()
    date_from = request.GET.get('from', '').strip()
    date_to = request.GET.get('to', '').strip()
    by = request.GET.get('by', '').strip()
    location = request.GET.get('location', '').strip()
    if not query:
        return HttpResponseRedirect('/')
    
    query_parts = query.split()

    notes_query = Q(title__icontains=query) | \
                  Q(created_by__username__icontains=query) | \
                  Q(created_by__first_name__icontains=query) | \
                  Q(created_by__last_name__icontains=query) | \
                  Q(tags__name__icontains=query) | \
                  Q(course__code__icontains=query) | \
                  Q(course__description__icontains=query) | \
                  Q(content__icontains=query)

    users_query = Q(username__icontains=query) | \
              Q(first_name__icontains=query) | \
              Q(last_name__icontains=query) | \
              Q(profile__bio__icontains=query) | \
              Q(email__icontains=query)

    if len(query_parts) > 1:
        notes_query |= Q(created_by__first_name__icontains=query_parts[0]) & Q(created_by__last_name__icontains=query_parts[1])
        users_query |= Q(first_name__icontains=query_parts[0]) & Q(last_name__icontains=query_parts[1])


    notes, tags, courses, users, authors, locations = [], [], [], [], [], []

    if category == 'notes':
        notes = Note.objects.filter(notes_query).distinct()
        authors = User.objects.filter(notes__in=notes).distinct()
        if by: notes = notes.filter(created_by__id=by)
        if date_from: notes = notes.filter(created_at__gte=date_from)
        if date_to: notes = notes.filter(created_at__lte=date_to)
    elif category == 'users':
        users = User.objects.filter(users_query).distinct()
        locations = User.objects.filter(users_query).values_list('profile__location', flat=True).distinct()
    elif category == 'courses':
        courses = Course.objects.filter(Q(code__icontains=query) | Q(description__icontains=query)).distinct()
        authors = User.objects.filter(courses__in=courses).distinct()
    elif category == 'tags':
        tags = Tag.objects.filter(name__icontains=query).distinct()
    else:
        notes = Note.objects.filter(notes_query).distinct()
        tags = Tag.objects.filter(notes__in=notes).distinct()
        courses = Course.objects.filter(Q(code__icontains=query) | Q(description__icontains=query)).distinct()
        users = User.objects.filter(users_query).distinct()

    return render(request, 'advanced_search/search_results.html', {
        'notes': notes,
        'tags': tags,
        'query': query,
        'title': 'Search results for: ' + (query[:8] + '...' if len(query) > 8 else query),
        'courses': courses,
        'users': users,
        'highlight':  query,
        'authors': authors,
        'locations': locations,
    })


def view_course(request, course_id):
    course = Course.objects.get(id=course_id)
    notes = Note.objects.filter(course=course)
    tags = Tag.objects.filter(notes__in=notes).distinct()
    return render(
        request,
        "advanced_search/search_results.html",
        {
            "notes": notes,
            "tags": tags,
            "title": course.code,
            "course": course,
        },
    )
