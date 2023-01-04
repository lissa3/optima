from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    """attrs: is_superuser,is_active,is_staff (let op: no is_admin)"""

    search_fields = ("email", "username")
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = (
        "id",
        "uuid",
        "email",
        "info",
        "last_login",
        "is_active",
        "is_superuser",
    )
    list_filter = ("is_active", "is_superuser")

    # add key 'classes' with value [collapse ] to toggle Permissions,Important Dates
    fieldsets = (
        ("User", {"fields": ("email", "password", "is_active")}),
        (
            "Permissions",
            {
                "classes": ["collapse"],
                "fields": (
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "Important dates",
            {"classes": ["collapse"], "fields": ("last_login", "date_joined")},
        ),
    )

    add_fieldsets = (
        (
            ("Add Your User"),
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "info"),
            },
        ),
    )
    ordering = ("-date_joined",)
    filter_horizontal = ("groups", "user_permissions")


admin.site.register(User, UserAdmin)
