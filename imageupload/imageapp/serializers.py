from rest_framework import serializers
from .models import Image
from versatileimagefield.serializers import VersatileImageFieldSerializer


class ImageSerializer(serializers.ModelSerializer):
    thumbnail_links = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = "__all__"

    def get_photo_url(self, obj):
        request = self.context.get("request")
        photo_url = obj.fingerprint.url
        return request.build_absolute_url(photo_url)

    def get_thumbnail_links(self, obj):
        return obj.get_thumbnail_links()
