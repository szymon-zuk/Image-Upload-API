from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Image, UserTier
from .serializers import ImageSerializer


class ImageCreateView(generics.CreateAPIView):
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ImageListView(generics.ListAPIView):
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(user=user)


class ImageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(user=user)
