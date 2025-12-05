from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import User, ParentProfile, Child


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """
    Админка для кастомного пользователя.
    Используем DjangoUserAdmin, но под наш User.
    """

    model = User

    list_display = ("email", "is_platform_admin", "is_staff", "is_active")
    list_filter = ("is_platform_admin", "is_staff", "is_active")
    search_fields = ("email",)
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Права доступа", {
            "fields": ("is_platform_admin", "is_staff", "is_active", "is_superuser"),
        }),
        ("Дополнительно", {"fields": ("date_joined",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2",
                       "is_platform_admin", "is_staff", "is_active"),
        }),
    )

    # чтобы админ не пытался искать groups / user_permissions
    filter_horizontal = ()


@admin.register(ParentProfile)
class ParentProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user")


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "parent")


