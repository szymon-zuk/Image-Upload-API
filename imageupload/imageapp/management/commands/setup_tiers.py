from django.core.management.base import BaseCommand
from imageapp.models import UserTier


class Command(BaseCommand):
    help = "Set up the built-in user tiers"

    def handle(self, *args, **kwargs):
        # Basic tier
        UserTier.objects.create(
            name="Basic",
            thumbnail_sizes={"200px": 200},
            original_link_enabled=False,
            expiring_link_enabled=False,
        )

        # Premium tier
        UserTier.objects.create(
            name="Premium",
            thumbnail_sizes={"200px": 200, "400px": 400},
            original_link_enabled=True,
            expiring_link_enabled=False,
        )

        # Enterprise tier
        UserTier.objects.create(
            name="Enterprise",
            thumbnail_sizes={"200px": 200, "400px": 400},
            original_link_enabled=True,
            expiring_link_enabled=True,
        )

        self.stdout.write(self.style.SUCCESS("Built-in tiers created successfully"))