
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['pk', 'username', 'first_name', 'last_name', 'is_staff', 'is_active']








