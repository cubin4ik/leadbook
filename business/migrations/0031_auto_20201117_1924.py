# Generated by Django 3.0.6 on 2020-11-17 16:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0025_auto_20201113_1640'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business', '0030_auto_20201116_1741'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reminder',
            new_name='Task',
        ),
    ]
