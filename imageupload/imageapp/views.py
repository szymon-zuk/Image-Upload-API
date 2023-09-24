import mimetypes
from django.http import FileResponse
from rest_framework import generics, permissions
from .permissions import IsSuperUserOrEnterprise
from rest_framework.exceptions import NotFound, PermissionDenied
from .models import Image, ExpiringLink
from django.conf import settings
from .serializers import (
    ImageListSerializer,
    ImageCreateSerializer,
    ExpiringLinkCreateSerializer,
    ExpiringLinkListSerializer,
)
from .mixins import ExpiringLinkMixin

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
    permission_classes = [IsSuperUserOrEnterprise]

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)


class ExpiringLinkListCreateView(generics.ListCreateAPIView, ExpiringLinkMixin):
    permission_classes = [IsSuperUserOrEnterprise]

    def get_queryset(self):
        return ExpiringLink.objects.filter(image__user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ExpiringLinkCreateSerializer
        return ExpiringLinkListSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = self.link
        return response

    def perform_create(self, serializer):
        expiration_time = self.request.data.get("expiration_time")
        self.link = self.generate_expiring_link(
            serializer.validated_data["image"], expiration_time
        )


class ExpiringLinkDetailsView(generics.RetrieveAPIView, ExpiringLinkMixin):
    permission_classes = [IsSuperUserOrEnterprise]
    queryset = ExpiringLink.objects.all()

    def get_object(self):
        signed_link = self.kwargs.get("signed_link")
        expiring_link = generics.get_object_or_404(self.queryset, link=signed_link)
        if expiring_link.is_link_expired():
            expiring_link.delete()
            raise NotFound("Link is already expired")
        if expiring_link.image.user != self.request.user:
            raise PermissionDenied("User doesn't have permission to see this link")

        return expiring_link.image
