# Generated by Django 3.0.6 on 2020-10-25 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0021_auto_20201025_2005'),
        ('business', '0022_auto_20201022_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='company_contractor',
        ),
        migrations.RemoveField(
            model_name='project',
            name='company_end_user',
        ),
        migrations.RemoveField(
            model_name='project',
            name='company_integrator',
        ),
        migrations.CreateModel(
            name='ProjectCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=500)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leads.Company')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='company',
            field=models.ManyToManyField(through='business.ProjectCompany', to='leads.Company'),
        ),
    ]
