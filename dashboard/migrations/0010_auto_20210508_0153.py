# Generated by Django 3.0.6 on 2021-05-07 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20210430_0129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='widget',
            name='url_path',
        ),
        migrations.AddField(
            model_name='widget',
            name='url_path_name',
            field=models.CharField(default='home', max_length=100),
        ),
    ]
