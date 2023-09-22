from rest_framework import serializers
from .models import UserTier, Image
from versatileimagefield.serializers import VersatileImageFieldSerializer


class UserTierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserTier
        fields = ("url", "id", "user", "tier")


class ImageSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail_200", "thumbnail__200x200"),
            ("thumbnail_400", "thumbnail__400x400"),
        ]
    )

    class Meta:
        model = Image
        fields = (
            "id",
            "user",
            "image",
            "expiration_seconds",
        )

        def get_photo_url(self, obj):
            request = self.context.get("request")
            photo_url = obj.fingerprint.url
            return request.build_absolute_url(photo_url)

        def get_image(self, obj):
            thumbnails = obj.get_all_images()
            thumbnails_to_return = []
            for thumbnail in thumbnails:
                thumbnails_to_return.append(thumbnail)

            return thumbnails_to_return
