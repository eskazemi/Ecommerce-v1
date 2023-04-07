from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import (
    UserCreateForm,
    UserChangeForm
)
from django.contrib.auth.models import Group
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm

    list_display = ('email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('Main', {
            'fields': ('email', 'phone_number', 'first_name', 'last_name', 'password')
        }),
        ('Permissions', {"fields": ('is_active', 'is_admin', 'last_login')}),
    )
    add_fieldsets = (
        (None, {"fields": ('email', 'phone_number', 'first_name', 'last_name', 'password', 'password_confirm')}),
    )
    search_fields = ('phone_number',)
    ordering = ('created_at',)
    filter_horizontal = ()


admin.site.unregister(Group)

admin.site.register(User, UserAdmin)
