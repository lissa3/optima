from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

UserAdmin.list_display += ("info",)
UserAdmin.fieldsets += (("User Info", {"fields": ("info",)}),)

admin.site.register(User, UserAdmin)
