# Generated by Django 5.0.6 on 2024-07-17 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_apicallhistory_file_path_apicallhistory_youtube_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apicallhistory',
            name='file_path',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='audiofile',
            name='file_path',
            field=models.CharField(max_length=1024),
        ),
    ]
