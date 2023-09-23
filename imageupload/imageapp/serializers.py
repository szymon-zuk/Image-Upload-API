import os

from django.utils.crypto import get_random_string
from rest_framework import serializers
from .models import Image, ExpiringLink
from versatileimagefield.serializers import VersatileImageFieldSerializer


class ImageListSerializer(serializers.ModelSerializer):
    image_links = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = (
            "id",
            "image_links",
        )

    def get_image_links(self, obj):
        base_url = "http://127.0.0.1:8000/"
        thumbnail_links = {}
        for key, thumbnail_url in obj.get_thumbnail_links().items():
            thumbnail_links[key] = f"{base_url}{thumbnail_url}"
        return thumbnail_links


class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("image",)


class ExpiringLinkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpiringLink
        fields = ("image", "expiration_time")

    def create(self, validated_data):
        image = validated_data.get("image")
        expiration_seconds = validated_data.get("expiration_time")
        link_identifier = get_random_string(length=32)
        link = f"/expiring/{link_identifier}"

        expiring_link_instance = ExpiringLink.objects.create(
            image=image, expiration_time=expiration_seconds, link=link
        )

        return expiring_link_instance


class ExpiringLinkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpiringLink
        fields = ("link",)
