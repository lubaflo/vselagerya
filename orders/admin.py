from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "shift", "amount", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("user__email", "child_name")
