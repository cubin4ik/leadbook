# Generated by Django 3.0.6 on 2020-09-01 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_auto_20200901_1203'),
        ('business', '0005_auto_20200901_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='company_end_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_end_user', to='leads.Company'),
        ),
        migrations.AlterField(
            model_name='project',
            name='company_integrator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_integrator', to='leads.Company'),
        ),
        migrations.AlterField(
            model_name='project',
            name='company_supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_supplier', to='leads.Company'),
        ),
    ]
