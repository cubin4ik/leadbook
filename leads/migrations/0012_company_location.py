# Generated by Django 3.0.6 on 2020-09-17 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0011_auto_20200916_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
