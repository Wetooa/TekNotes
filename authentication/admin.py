from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentication.models import Users

admin.site.register(Users, UserAdmin)
# Register your models here.
