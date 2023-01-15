# Generated by Django 4.2 on 2023-01-15 07:50

import django_better_admin_arrayfield.models.fields

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("anime", "0004_alter_animemodel_anime_banner_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animemodel",
            name="anime_name_synonyms",
            field=django_better_admin_arrayfield.models.fields.ArrayField(
                base_field=models.CharField(max_length=1024),
                blank=True,
                null=True,
                size=None,
            ),
        ),
    ]