from rest_framework import serializers
from .models import UserTier, Image


class UserTierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserTier
        fields = ("url", "id", "user", "tier")


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            "id",
            "user",
            "image",
            "uploaded",
            "is_thumbnail_generated",
            "is_expiring_link_enabled",
            "expiration_seconds",
        )
