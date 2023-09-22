import os.path

from django.db import models
from django.contrib.auth.models import User
from versatileimagefield.fields import VersatileImageField


class ThumbnailSizes(models.Model):
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.width}x{self.height}"


class Tier(models.Model):
    name = models.CharField(max_length=255, default="Basic")
    thumbnail_sizes = models.ManyToManyField(ThumbnailSizes, blank=True)
    original_link_enabled = models.BooleanField(default=False)
    expiring_link_enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def get_thumbnail_sizes(self):
        return self.thumbnail_sizes.all()

    @property
    def get_available_heights(self):
        thumbnails = self.get_thumbnail_sizes
        return [thumbnail.height for thumbnail in thumbnails]


class UserTier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    tier = models.ForeignKey(Tier, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"User: {self.user.username} - Tier: {self.tier}"


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = VersatileImageField(upload_to="images/")
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
        tier = self.user.tier
        thumbnail_links = {}

        for thumbnail_size in tier.thumbnail_sizes.all():
            size_key = f"{thumbnail_size.width}px_height"
            thumbnail_links[size_key] = self.image.crop[
                thumbnail_size.width, thumbnail_size.height
            ].url

        if tier.original_link_enabled:
            thumbnail_links["original"] = self.image.url

        return thumbnail_links
