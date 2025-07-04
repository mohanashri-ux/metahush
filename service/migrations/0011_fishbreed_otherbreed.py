# Generated by Django 5.1.7 on 2025-06-14 10:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0010_catbreed"),
    ]

    operations = [
        migrations.CreateModel(
            name="FishBreed",
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
                ("name", models.CharField(max_length=100)),
                ("origin", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("small", "Small"),
                            ("medium", "Medium"),
                            ("large", "Large"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="fish_breeds/"),
                ),
                ("slug", models.SlugField(unique=True)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fish_breeds",
                        to="service.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OtherBreed",
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
                ("name", models.CharField(max_length=100)),
                ("origin", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("small", "Small"),
                            ("medium", "Medium"),
                            ("large", "Large"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="other_breeds/"),
                ),
                ("slug", models.SlugField(unique=True)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="other_breeds",
                        to="service.category",
                    ),
                ),
            ],
        ),
    ]
