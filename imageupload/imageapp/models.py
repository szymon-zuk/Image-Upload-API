from django.db import models
from django.contrib.auth.models import User


class Tier(models.Model):
    name = models.CharField(max_length=255, default="Basic")
    thumbnail_sizes = models.JSONField(default=dict)
    original_link_enabled = models.BooleanField(default=False)
    expiring_link_enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class UserTier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    tier = models.ForeignKey(Tier, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"User: {self.user.username} - Tier: {self.tier}"


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/images/")
    uploaded = models.DateTimeField(auto_now_add=True)
    is_thumbnail_generated = models.BooleanField(default=False)
    is_expiring_link_enabled = models.BooleanField(default=False)
    expiration_seconds = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Set this parameter in seconds between 300 and 30000",
    )

    def __str__(self):
        return f"User: {self.user.username} - Image: {self.image.name}"
