import uuid
from random import randint
from django.core import signing
from django.urls import reverse
import time
from .models import ExpiringLink
from rest_framework.exceptions import NotFound


class ExpiringLinkMixin:
    def generate_expiring_link(self, image, expiration_time):
        pk = randint(1, 10000)
        signed_link = signing.dumps(str(pk))

        full_url = self.request.build_absolute_uri(
            reverse("expiring-link-detail", kwargs={"signed_link": signed_link})
        )

        ExpiringLink.objects.create(
            id=pk, link=full_url, image=image, expiration_time=expiration_time
        )

        return {"link": full_url}

    @staticmethod
    def decode_signed_value(value):
        """Decodes signed link."""
        try:
            return signing.loads(value)
        except signing.BadSignature:
            raise NotFound("Invalid signed link")
