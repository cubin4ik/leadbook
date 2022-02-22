# Generated by Django 3.0.6 on 2021-04-28 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leads', '0029_auto_20210427_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='created_by',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='company_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='company',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_manager', to=settings.AUTH_USER_MODEL),
        ),
    ]
