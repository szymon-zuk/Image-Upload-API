from django.contrib import admin
from .models import Image, ExpiringLink


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("user", "image")


admin.site.register(ExpiringLink)
