# Generated by Django 4.0.4 on 2022-04-25 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("anime", "0017_alter_episodetimestampmodel_episode"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="episodetimestampmodel",
            name="episode",
        ),
    ]
