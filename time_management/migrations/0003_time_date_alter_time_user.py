# Generated by Django 5.1.6 on 2025-05-21 17:13

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_management', '0002_time_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='time',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='time',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
