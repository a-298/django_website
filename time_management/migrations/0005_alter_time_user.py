# Generated by Django 5.1.6 on 2025-05-23 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_management', '0004_rename_pc_time_time_computer_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
