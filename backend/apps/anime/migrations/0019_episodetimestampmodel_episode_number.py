# Generated by Django 4.0.4 on 2022-04-25 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("anime", "0018_remove_episodetimestampmodel_episode"),
    ]

    operations = [
        migrations.AddField(
            model_name="episodetimestampmodel",
            name="episode_number",
            field=models.PositiveBigIntegerField(db_index=True, null=True),
        ),
    ]
