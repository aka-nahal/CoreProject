# Generated by Django 4.1.2 on 2022-10-09 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("characters", "0004_characterlogmodel"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CharacterLogModel",
        ),
    ]