from django.contrib import admin
from .models import Click, ClickCourse, ClickNote, ClickTag

admin.site.register(Click)
admin.site.register(ClickCourse)
admin.site.register(ClickNote)
admin.site.register(ClickTag)