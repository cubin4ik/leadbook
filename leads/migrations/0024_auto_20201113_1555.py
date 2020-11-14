# Generated by Django 3.0.6 on 2020-11-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0023_auto_20201113_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='area_code',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='country_code',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='extension',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='number',
            field=models.PositiveIntegerField(),
        ),
    ]
