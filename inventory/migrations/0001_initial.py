# Generated by Django 5.0.3 on 2024-03-22 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("vendor", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Products",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("price", models.FloatField(default=0.0)),
                ("image", models.ImageField(blank=True, upload_to="product_image")),
                ("description", models.TextField(blank=True)),
                ("stock", models.IntegerField(default=0)),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vendor_product",
                        to="vendor.vendor",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]