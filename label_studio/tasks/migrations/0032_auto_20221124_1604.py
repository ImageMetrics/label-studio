# Generated by Django 3.2.16 on 2022-11-24 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0031_auto_20221118_2338'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['total_annotations'], name='task_total_a_bc99f8_idx'),
        ),
    ]
