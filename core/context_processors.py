from django.db.models import Count
from course.models import Course
from clicks.models import ClickNote, ClickTag, ClickCourse



def courses_list(request):
    return {"your_courses": Course.objects.all().distinct()}


def trending(request):
    trending_notes = (
        ClickNote.objects.prefetch_related("note")
        .annotate(click_count=Count("id"))
        .order_by("-click_count")
    )[:5]

    trending_tags = (
        ClickTag.objects.prefetch_related("tag")
        .annotate(click_count=Count("id"))
        .order_by("-click_count")
    )[:5]

    trending_courses = (
        ClickCourse.objects.prefetch_related("course")
        .annotate(click_count=Count("id"))
        .order_by("-click_count")
    )[:5]

    return {
        "trending_notes": trending_notes,
        "trending_tags": trending_tags,
        "trending_courses": trending_courses,
    }


def recent_posts(request):
    return {}


def notifications(request):
    return {}
