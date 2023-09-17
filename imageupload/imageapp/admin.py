from django.contrib import admin
from .models import UserTier, Image


@admin.register(UserTier)
class UserTierAdmin(admin.ModelAdmin):
    list_display = ("user", "tier")


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("user", "image")
