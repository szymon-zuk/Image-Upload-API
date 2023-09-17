from django.db import models
from django.contrib.auth.models import User

TIER_TYPES = [
    ("Basic", "Basic"),
    ("Premium", "Premium"),
    ("Enterprise", "Enterprise"),
]


class UserTier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tier = models.CharField(max_length=30, choices=TIER_TYPES)

    def __str__(self):
        return self.user.username


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
