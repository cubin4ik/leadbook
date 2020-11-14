# Generated by Django 3.0.6 on 2020-11-02 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0021_auto_20201025_2005'),
        ('business', '0026_auto_20201028_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcompany',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.Company'),
        ),
        migrations.AlterField(
            model_name='projectcompany',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Project'),
        ),
    ]