from django.contrib import admin
from .models import UserTier, Image, Tier


@admin.register(UserTier)
class UserTierAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "tier",
    )


@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "thumbnail_sizes",
        "original_link_enabled",
        "expiring_link_enabled",
    )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("user", "image")
