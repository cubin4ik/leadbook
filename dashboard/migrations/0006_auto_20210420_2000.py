# Generated by Django 3.0.6 on 2021-04-20 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20210327_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('url_path', models.URLField()),
                ('size', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Widgets',
        ),
    ]
