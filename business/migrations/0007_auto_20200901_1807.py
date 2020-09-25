# Generated by Django 3.0.6 on 2020-09-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_auto_20200901_1504'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='project',
            name='volume',
            field=models.IntegerField(blank=True, help_text='Estimated project volume in euros', null=True),
        ),
    ]