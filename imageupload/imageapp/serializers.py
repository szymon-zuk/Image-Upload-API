import os
from rest_framework import serializers
from .models import Image
from versatileimagefield.serializers import VersatileImageFieldSerializer


class ImageListSerializer(serializers.ModelSerializer):
    image_links = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ("image_links",)

    def get_image_links(self, obj):
        base_url = f"http://127.0.0.1:8000/"
        thumbnail_links = {}
        for key, thumbnail_url in obj.get_thumbnail_links().items():
            thumbnail_links[key] = f"{base_url}{thumbnail_url}"
        return thumbnail_links


class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("image",)
