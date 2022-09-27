# Generated by Django 4.1 on 2022-08-17 06:44

from django.db import migrations, models

import apps.characters.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CharacterModel",
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
                ("mal_id", models.IntegerField(db_index=True, unique=True)),
                (
                    "kitsu_id",
                    models.IntegerField(db_index=True, null=True, unique=True),
                ),
                (
                    "anilist_id",
                    models.IntegerField(db_index=True, null=True, unique=True),
                ),
                ("name", models.CharField(db_index=True, max_length=1024)),
                (
                    "name_kanji",
                    models.CharField(blank=True, db_index=True, max_length=1024, null=True),
                ),
                (
                    "character_image",
                    models.ImageField(
                        blank=True,
                        default=None,
                        null=True,
                        upload_to=apps.characters.models.FileField.anime_charater,
                    ),
                ),
                ("about", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Character",
                "verbose_name_plural": "Characters",
            },
        ),
    ]