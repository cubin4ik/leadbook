# Generated by Django 3.0.6 on 2021-05-05 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0030_auto_20210428_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='is_main_contact',
            field=models.BooleanField(default=False),
        ),
    ]
