from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Image
from users.models import UserAccountTier
from django.core.files.uploadedfile import SimpleUploadedFile


class ImageAPITestCase(APITestCase):
    def setUp(self):
        enterprise = UserAccountTier.objects.get(id=3)
        self.user = get_user_model().objects.create_user(
            username="test user", password="test password", tier=enterprise
        )
        self.client.force_login(user=self.user)
        self.image = Image.objects.create(
            image=SimpleUploadedFile(
                name="test_image.jpeg", content=b"content", content_type="image/jpeg"
            ),
        )

    def test_list_images_method_get(self):
        response = self.client.get(reverse("image-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
