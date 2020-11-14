# Generated by Django 3.0.6 on 2020-11-13 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0021_auto_20201025_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='area_code',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='phone',
            name='country_code',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='phone',
            name='extension',
            field=models.IntegerField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='number',
            field=models.IntegerField(max_length=15),
        ),
    ]
