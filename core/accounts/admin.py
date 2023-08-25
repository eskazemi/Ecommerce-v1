from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import (
    UserCreateForm,
    UserChangeForm
)
from django.contrib.auth.models import Group
from .models import (
    User,
    OtpCode,
)


@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "code", "created_at")


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm

    list_display = ('email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('Main', {
            'fields': ('email', 'phone_number', 'first_name', 'last_name', 'password')
        }),
        ('Permissions', {"fields": ('is_active',
                                    'is_admin',
                                    'is_superuser',
                                    'last_login',
                                    'groups',
                                    'user_permissions')
                         }),
    )
    add_fieldsets = (
        (None, {"fields": ('email', 'phone_number', 'first_name', 'last_name', 'password', 'password_confirm')}),
    )
    search_fields = ('phone_number',)
    ordering = ('created_at',)
    filter_horizontal = ('groups', 'user_permissions')
    readonly_fields = ('last_login',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj=None, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields['is_superuser'].disable = True
        return form


admin.site.unregister(Group)

admin.site.register(User, UserAdmin)
