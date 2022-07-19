# Generated by Django 4.0.6 on 2022-07-17 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('linkoapp', '0035_alter_post_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucketlist',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='linkoapp.portrait'),
        ),
        migrations.AlterField(
            model_name='bucketlist',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]