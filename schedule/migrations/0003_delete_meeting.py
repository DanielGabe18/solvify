# Generated by Django 5.0 on 2024-01-01 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_remove_meeting_created_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Meeting',
        ),
    ]
