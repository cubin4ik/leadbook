# Generated by Django 3.0.6 on 2021-04-20 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20210420_2000'),
        ('accounts', '0004_auto_20210327_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='widgets',
            field=models.ManyToManyField(to='dashboard.Widget'),
        ),
    ]
