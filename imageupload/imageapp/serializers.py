from rest_framework import serializers
from .models import UserTier, Image
from versatileimagefield.serializers import VersatileImageFieldSerializer


class UserTierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserTier
        fields = ("url", "id", "user", "tier")


class ImageSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes="sizes")

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

        def get_photo_url(self, obj):
            request = self.context.get("request")
            photo_url = obj.fingerprint.url
            return request.build_absolute_url(photo_url)
