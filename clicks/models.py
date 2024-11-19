from django.db import models
from notes.models import Note
from tags.models import Tag
from course.models import Course
from django.contrib.auth.models import User

# Create your models here.


class Click(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            (self.user if self.user else "Anon")
            + " clicked during "
            + str(self.created_at)
        )


class ClickNote(Click):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__() + " on note " + self.note.title


class ClickTag(Click):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__() + " on tag" + self.tag.title


class ClickCourse(Click):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__() + " on course" + self.course.title
