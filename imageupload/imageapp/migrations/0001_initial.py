# Generated by Django 4.2.5 on 2023-09-23 08:01

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    versatileimagefield.fields.VersatileImageField(upload_to="images/"),
                ),
                ("uploaded", models.DateTimeField(auto_now_add=True)),
                ("original_file_enabled", models.BooleanField(default=False)),
                ("expiring_link_enabled", models.BooleanField(default=False)),
                (
                    "expiration_seconds",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="Set this parameter in seconds between 300 and 30000",
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ThumbnailSizes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("width", models.PositiveIntegerField()),
                ("height", models.PositiveIntegerField()),
            ],
        ),
    ]
