# Generated by Django 4.2.5 on 2023-09-08 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lead",
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
                ("name", models.TextField()),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("prospect", "Prospect"),
                            ("active", "Active"),
                            ("unqualified", "Unqualified"),
                        ],
                        default="prospect",
                        max_length=20,
                    ),
                ),
                (
                    "estimatedSaleAmount",
                    models.DecimalField(decimal_places=2, max_digits=15),
                ),
                (
                    "estimatedCommission",
                    models.DecimalField(decimal_places=2, max_digits=15),
                ),
            ],
        ),
    ]