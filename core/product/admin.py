from django.contrib import admin
from .models import (
    Product,
    Category,
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "price", "is_available")
    raw_id_fields = ('category',)
    search_fields = ("name",)
    list_filter = ("is_available",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", 'is_sub')
    search_fields = ("name",)
    list_filter = ("is_sub",)



