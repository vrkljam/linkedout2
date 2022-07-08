# Generated by Django 4.0.6 on 2022-07-08 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('linkoapp', '0004_profile_post_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.ForeignKey(default='?', on_delete=django.db.models.deletion.CASCADE, to='linkoapp.profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.ForeignKey(default='?', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
