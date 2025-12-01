from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User

    list_display = ("email", "full_name", "role", "is_staff")
    list_filter = ("role", "is_staff", "is_active")

    ordering = ("email",)

    search_fields = ("email", "full_name")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Персональная информация", {"fields": ("full_name", "role")}),
        ("Права доступа", {"fields": ("is_staff", "is_active", "is_superuser")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "role", "is_staff", "is_active")}
         ),
    )
