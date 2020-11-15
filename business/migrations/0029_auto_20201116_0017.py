# Generated by Django 3.0.4 on 2020-11-15 21:17

import business.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0028_auto_20201112_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(choices=[('TEL', 'Phone call'), ('EMAIL', 'Email'), ('MEET', 'Meeting'), ('SKYPE', 'Skype call'), ('CONF', 'Conference'), ('TRAIN', 'Training'), ('ORDER', 'Order'), ('INCID', 'Incident'), ('FAIR', 'Trade fair'), ('FORUM', 'Forum')], default='EMAIL', max_length=5),
        ),
        migrations.CreateModel(
            name='ProjectDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to=business.models.project_file_path)),
                ('description', models.CharField(max_length=500)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Project')),
            ],
        ),
    ]
