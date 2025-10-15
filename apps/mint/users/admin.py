from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "guild", "is_staff", "created_at")
    list_filter = ("is_staff", "is_superuser", "is_active", "guild")
    search_fields = ("username", "email")
    ordering = ("-created_at",)

    fieldsets = BaseUserAdmin.fieldsets + (
        ("Mint", {"fields": ("guild", "created_at", "updated_at")}),
    )
    readonly_fields = ("created_at", "updated_at")
