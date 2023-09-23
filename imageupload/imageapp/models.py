import os.path
from django.conf import settings
from django.db import models
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer


User = settings.AUTH_USER_MODEL


class ThumbnailSizes(models.Model):
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.width}x{self.height}"


class DynamicRenditionVersatileImageField(VersatileImageField):
    def create_images(self, image, *args, **kwargs):
        rendition_key_set = []

        thumbnail_sizes = ThumbnailSizes.objects.all()

        for size in thumbnail_sizes:
            key = f"{size.width}x{size.height}"
            rendition_key_set.append((key, f"crop__{size.width}x{size.height}"))

        kwargs["rendition_key_set"] = rendition_key_set
        return super().create_images(image, *args, **kwargs)


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = DynamicRenditionVersatileImageField(upload_to="images/")
    uploaded = models.DateTimeField(auto_now_add=True)
    original_file_enabled = models.BooleanField(default=False)
    expiring_link_enabled = models.BooleanField(default=False)
    expiration_seconds = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Set this parameter in seconds between 300 and 30000",
    )

    def __str__(self):
        return f"User: {self.user.username} - Image: {self.image.name}"

    @property
    def get_original_url(self):
        return self.image.url

    def get_thumbnail_links(self):
        user_tier = self.user.tier

        thumbnail_links = {}

        if user_tier and user_tier.tier:
            rendition_key_set = []
            for thumbnail_size in self.user.tier.thumbnail_sizes.all():
                width = int(thumbnail_size.width)
                height = int(thumbnail_size.height)
                size = f"{width}x{height}"
                rendition_key_set.append((size, size))

            for key, size in rendition_key_set:
                thumbnail = self.image.crop[size]
                thumbnail_url = thumbnail.url
                thumbnail_links[key] = thumbnail_url

            if user_tier.original_link_enabled:
                thumbnail_links["original_image"] = self.image.url

            return thumbnail_links
