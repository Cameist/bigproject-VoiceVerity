# Generated by Django 5.0.6 on 2024-07-05 03:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0012_alter_subscriptionplan_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                ("tid", models.CharField(max_length=100)),
                (
                    "next_redirect_app_url",
                    models.URLField(blank=True, max_length=500, null=True),
                ),
                (
                    "next_redirect_mobile_url",
                    models.URLField(blank=True, max_length=500, null=True),
                ),
                (
                    "next_redirect_pc_url",
                    models.URLField(blank=True, max_length=500, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("status", models.CharField(default="initiated", max_length=20)),
                (
                    "plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.subscriptionplan",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
