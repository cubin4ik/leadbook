# Generated by Django 3.0.6 on 2021-03-27 13:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Widgets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('url_path', models.URLField()),
                ('value', models.IntegerField()),
                ('account', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
