from rest_framework import generics, permissions
from .models import Image
from django.conf import settings
from .serializers import ImageListSerializer, ImageCreateSerializer

User = settings.AUTH_USER_MODEL


class ImageCreateView(generics.CreateAPIView):
    serializer_class = ImageCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ImageListView(generics.ListAPIView):
    serializer_class = ImageListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)


class ImageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImageListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)
