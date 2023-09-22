from django.contrib import admin
from .models import UserTier, Image, Tier, ThumbnailSizes


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
        "original_link_enabled",
        "expiring_link_enabled",
    )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("user", "image")


@admin.register(ThumbnailSizes)
class ThumbnailSizesAdmin(admin.ModelAdmin):
    list_display = ("width", "height")
