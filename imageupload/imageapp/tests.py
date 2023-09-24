import os
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from PIL import ImageDraw
from PIL import Image as PILImage
from imageapp.models import Image, ExpiringLink, ThumbnailSizes
from users.models import Tier
from django.core.files.uploadedfile import SimpleUploadedFile


def create_test_image():
    test_file = SimpleUploadedFile(
        name="test_image.jpg",
        content=b"",
        content_type="image/jpeg",
    )
    return test_file


class ImageAPITestCase(APITestCase):
    def setUp(self):
        enterprise_acc = Tier.objects.create(
            name="Enterprise", original_link_enabled=True, expiring_link_enabled=True
        )
        self.user = get_user_model().objects.create_user(
            username="test user", password="test password", tier=enterprise_acc
        )
        self.client.login(username="test user", password="test password")
        self.image = create_test_image()

    def test_list_images_method_get(self):
        Image.objects.create(user=self.user, image=self.image)
        response = self.client.get(reverse("image-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_images_method_post(self):
        payload = {"image": self.image}
        response = self.client.post(
            reverse("create-image"), payload, format="multipart"
        )
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Image.objects.count(), 1)
