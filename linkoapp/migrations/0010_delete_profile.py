# Generated by Django 4.0.6 on 2022-07-08 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linkoapp', '0009_rename_username_profile_testing'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]