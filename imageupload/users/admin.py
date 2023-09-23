from django.contrib import admin
from .models import Tier, ThumbnailSizes, UserAccountTier


@admin.register(UserAccountTier)
class UserAccountTierAdmin(admin.ModelAdmin):
    list_display = ("username", "tier")


@admin.register(ThumbnailSizes)
class ThumbnailSizesAdmin(admin.ModelAdmin):
    list_display = ("width", "height")


@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "original_link_enabled",
        "expiring_link_enabled",
    )
