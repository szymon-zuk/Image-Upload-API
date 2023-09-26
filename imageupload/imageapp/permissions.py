from rest_framework.permissions import BasePermission


class IsSuperUserOrEnterprise(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or (
            request.user.is_authenticated
            and request.user.account_tier.name == "Enterprise"
        )
