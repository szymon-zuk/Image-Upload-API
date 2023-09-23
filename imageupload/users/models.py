from django.db import models
from django.contrib.auth.models import AbstractUser
from imageapp.models import ThumbnailSizes


class UserAccountTier(AbstractUser):
    tier = models.ForeignKey(
        "Tier", on_delete=models.SET_NULL, null=True, related_name="tier"
    )


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
