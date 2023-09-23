from django.core.management.base import BaseCommand
from imageapp.models import Tier, ThumbnailSizes


class Command(BaseCommand):
    help = "Set up the built-in user tiers"

    def handle(self, *args, **kwargs):
        thumbnail_sizes_200px = ThumbnailSizes.objects.create(width=200, height=200)
        thumbnail_sizes_400px = ThumbnailSizes.objects.create(width=400, height=400)

        # Basic tier
        basic_tier = Tier.objects.create(
            name="Basic",
            original_link_enabled=False,
            expiring_link_enabled=False,
        )
        basic_tier.thumbnail_sizes.add(thumbnail_sizes_200px)

        # Premium tier
        premium_tier = Tier.objects.create(
            name="Premium",
            original_link_enabled=True,
            expiring_link_enabled=False,
        )
        premium_tier.thumbnail_sizes.add(thumbnail_sizes_200px, thumbnail_sizes_400px)

        # Enterprise tier
        enterprise_tier = Tier.objects.create(
            name="Enterprise",
            original_link_enabled=True,
            expiring_link_enabled=True,
        )
        enterprise_tier.thumbnail_sizes.add(thumbnail_sizes_200px, thumbnail_sizes_400px)

        self.stdout.write(self.style.SUCCESS("Built-in tiers created successfully"))

