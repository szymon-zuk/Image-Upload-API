import os
from rest_framework import serializers
from .models import Image, ExpiringLink
from versatileimagefield.serializers import VersatileImageFieldSerializer
from .utils import generate_expiring_link


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


class ExpiringLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpiringLink
        fields = ("image", "expiration_time")

    def create(self, validated_data):
        image = validated_data.get("image")
        expiration_time = validated_data.get("expiration_time")

        expiring_link = generate_expiring_link(image, expiration_time)
        validated_data["link"] = expiring_link
        expiring_link_instance = ExpiringLink.objects.create(**validated_data)

        return expiring_link_instance
