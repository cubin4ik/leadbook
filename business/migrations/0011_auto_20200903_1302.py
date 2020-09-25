# Generated by Django 3.0.6 on 2020-09-03 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0010_auto_20200901_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectStage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AddField(
            model_name='project',
            name='stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.ProjectStage'),
        ),
    ]