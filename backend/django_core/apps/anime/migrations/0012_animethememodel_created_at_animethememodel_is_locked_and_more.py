# Generated by Django 4.2 on 2023-04-24 15:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("anime", "0011_animegenremodel_created_at_animegenremodel_is_locked_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="animethememodel",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="animethememodel",
            name="is_locked",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="animethememodel",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
