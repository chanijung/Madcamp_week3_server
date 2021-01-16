from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# admin.site.register(models.User)
@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("CustomProfile", {
        "fields": (
            "nickname",
            "login_method",
            "uid",
        )
    }), )

    list_display = (
        "username",
        "uid",
        "nickname",
        "login_method",
    )