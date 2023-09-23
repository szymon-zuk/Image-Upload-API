import hashlib
import random
import time
from django.utils.crypto import get_random_string
from .models import ExpiringLink


def generate_expiring_link(image, expiration_seconds):
    link_identifier = get_random_string(length=32)

    current_time = int(time.time())
    expiration_time = current_time + expiration_seconds

    link = f"/expiring/{link_identifier}"

    expiring_link = ExpiringLink.objects.create(
        image=image, expiration_time=expiration_time, link=link
    )

    return expiring_link.link
