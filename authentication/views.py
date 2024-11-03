from django.shortcuts import render, redirect
from django.contrib.auth import logout as log_out
from django.db.models import OuterRef, Subquery

from course.models import Course
from authentication.forms import RegisterForm
from authentication.models import Profile
from notes.models import Note
from comments.models import Like


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            Profile.objects.create(user=user)

            return redirect("/authentication/login/")
    else:
        form = RegisterForm()

    return render(request, "authentication/register.html", {"form": form})


def logout(request):
    log_out(request)
    return redirect("/")


def profile(request, user_id):
    profile = Profile.objects.get(user__id=user_id)
    notes = Note.objects.filter(created_by=user_id, is_private=False)

    return render(
        request,
        "authentication/profile.html",
        {
            "profile": profile,
            "notes": notes,
        },
    )


def profile_likes(request, user_id):
    profile = Profile.objects.get(user__id=user_id)
    latest_likes = Like.objects.filter(note=OuterRef("pk"), user__id=user_id).order_by(
        "-created_at"
    )
    notes = (
        Note.objects.filter(likes__user__id=user_id, is_private=False)
        .annotate(like_created_at=Subquery(latest_likes.values("created_at")[:1]))
        .distinct()
        .order_by("-like_created_at")
    )

    return render(
        request, "authentication/profile.html", {"profile": profile, "notes": notes}
    )


def profile_courses(request, user_id):
    profile = Profile.objects.get(user__id=user_id)
    courses = Course.objects.filter(created_by__id=user_id).distinct()

    return render(
        request,
        "authentication/profile.html",
        {
            "profile": profile,
            "courses": courses,
        },
    )
