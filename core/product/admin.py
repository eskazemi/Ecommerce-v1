from django.contrib import admin
from .models import (
    Product,
    Category,
)


@admin.register(Product)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "category")


@admin.register(Category)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


