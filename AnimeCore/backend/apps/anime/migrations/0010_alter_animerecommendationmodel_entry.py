# Generated by Django 4.0.3 on 2022-04-03 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("anime", "0009_alter_animeinfomodel_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animerecommendationmodel",
            name="entry",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="anime.animeinfomodel",
            ),
        ),
    ]
