# Generated by Django 3.0.6 on 2020-10-28 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0025_auto_20201028_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcompany',
            name='role',
            field=models.CharField(choices=[('CTR', 'Contractor'), ('INT', 'Integrator'), ('EUS', 'End User')], default='CTR', max_length=3),
        ),
    ]
