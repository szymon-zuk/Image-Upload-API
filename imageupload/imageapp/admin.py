from django.contrib import admin
from .models import UserTier, Image


@admin.register(UserTier)
class UserTierAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "thumbnail_sizes",
        "original_link_enabled",
        "expiring_link_enabled",
    )
    list_filter = ("original_link_enabled", "expiring_link_enabled")


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("user", "image")
