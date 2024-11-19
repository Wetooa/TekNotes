from course.models import Course


def courses_list(request):
    return {"your_courses": Course.objects.all().distinct()}

