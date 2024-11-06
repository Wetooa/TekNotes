from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.contrib.auth import logout as log_out
from django.db.models import OuterRef, Subquery
from django.contrib.auth.decorators import login_required

from course.models import Course
from .forms import RegisterForm
from .models import Profile
from notes.models import Note
from comments.models import Like

from django.dispatch import receiver
from allauth.account.signals import user_signed_up


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
    return redirect("/auth/login/")


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


@receiver(user_signed_up)
def create_profile_on_google_signup(request, user, **kwargs):
    Profile.objects.create(user=user)


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


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        if "avatar" in request.FILES:
            profile.avatar = request.FILES["avatar"]
        profile.user.first_name = request.POST.get(
            "first_name", profile.user.first_name
        )
        profile.user.last_name = request.POST.get("last_name", profile.user.last_name)
        profile.bio = request.POST.get("bio", profile.bio)
        profile.location = request.POST.get("location", profile.location)

        profile.user.save()
        profile.save()

        return redirect("authentication:profile", user_id=request.user.id)
    else:
        return render(request, "authentication/edit_profile.html", {"profile": profile})
