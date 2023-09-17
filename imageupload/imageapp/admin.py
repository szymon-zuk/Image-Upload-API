from django.contrib import admin
from .models import UserTier


@admin.register(UserTier)
class UserTierAdmin(admin.ModelAdmin):
    list_display = ("user", "tier")
