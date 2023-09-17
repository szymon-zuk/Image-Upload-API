from django.db import models
from django.contrib.auth.models import User


class UserTier(models.Model):
    name = models.CharField(max_length=255, default="Basic")
    thumbnail_sizes = models.JSONField(default=dict)
    original_link_enabled = models.BooleanField(default=False)
    expiring_link_enabled = models.BooleanField(default=False)
    users = models.ManyToManyField(User, related_name="user_tier", blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
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
