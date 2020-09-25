# Generated by Django 3.0.6 on 2020-09-09 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_auto_20200909_1640'),
        ('business', '0012_auto_20200904_1304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['registry_date']},
        ),
        migrations.AddField(
            model_name='project',
            name='short_description',
            field=models.CharField(default='Россия', help_text="Short description like facility's title", max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='company_contractor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_contractor', to='leads.Company'),
        ),
        migrations.AlterField(
            model_name='project',
            name='location',
            field=models.CharField(help_text='City of the project', max_length=100),
        ),
    ]
