from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['pkid', 'id', 'email', 'first_name', 'last_name','phone_number', 'is_staff', 'is_active']
    list_display_links = ['id', 'email']
    list_filter = ['email', 'first_name', 'last_name','phone_number', 'is_staff', 'is_active']
    fieldsets = (
        (_("Login Credentials"), {
            "fields": (
                "email",
                "password",
            ),
        }),
        (_("Personal Information"), {
            "fields": (
                "first_name",
                "last_name",
                "phone_number",
            )
        }),
        (_("Permission and Groups"), {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        (_("Important Dates"), {
            "fields": (
                "last_login",
                "date_joined"
            )
        })

    )

    search_fields = ["email", "firstname", "lastname", "phone_number"]

admin.site.register(User, UserAdmin)