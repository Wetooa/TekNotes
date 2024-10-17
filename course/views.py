from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from course.models import Course
from .forms import CourseForm

@login_required
def add_a_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.created_by = request.user
            course.save()
            return HttpResponseRedirect('/')
    else:
        form = CourseForm()

    return render(request, 'course/add_a_course.html', {'form': form})

@login_required
def delete_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id, created_by=request.user)
        course.delete()
        return HttpResponseRedirect('/')
    except Course.DoesNotExist:
        return HttpResponseRedirect('/course/not_found/')
