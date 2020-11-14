# Generated by Django 3.0.6 on 2020-11-12 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0027_auto_20201102_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='code',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='projectcompany',
            name='role',
            field=models.CharField(choices=[('CTR', 'Contractor'), ('INT', 'Integrator'), ('EUS', 'End User'), ('PRT', 'Partner')], default='CTR', max_length=3),
        ),
    ]