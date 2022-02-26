# Generated by Django 3.0.6 on 2021-03-27 13:57

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210314_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(default='users/default_profile_img.png', upload_to=accounts.models.user_image_path),
        ),
    ]