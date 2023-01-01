# Generated by Django 4.1.4 on 2022-12-28 07:49

import functools

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.crypto


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial_"),
    ]

    operations = [
        migrations.CreateModel(
            name="Token",
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
                    "token",
                    models.CharField(
                        default=functools.partial(
                            django.utils.crypto.get_random_string, *(16,), **{}
                        ),
                        editable=False,
                        max_length=16,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "token",
                "verbose_name_plural": "tokens",
                "db_table": "user_token",
            },
        ),
    ]