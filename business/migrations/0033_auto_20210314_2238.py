# Generated by Django 3.0.6 on 2021-03-14 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0032_auto_20201117_2047'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectcompany',
            options={'ordering': ['-project__registry_date']},
        ),
    ]