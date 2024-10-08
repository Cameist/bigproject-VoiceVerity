# Generated by Django 5.0.6 on 2024-07-05 03:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0013_payment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payment",
            name="next_redirect_app_url",
        ),
        migrations.RemoveField(
            model_name="payment",
            name="next_redirect_mobile_url",
        ),
        migrations.RemoveField(
            model_name="payment",
            name="next_redirect_pc_url",
        ),
        migrations.AddField(
            model_name="payment",
            name="amount",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="payment",
            name="tid",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
