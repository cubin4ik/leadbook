# Generated by Django 3.0.6 on 2020-10-19 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0020_auto_20201019_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(choices=[('TEL', 'Phone call'), ('EMAIL', 'Email'), ('MEET', 'Meeting'), ('SKYPE', 'Skype call'), ('CONF', 'Conference'), ('TRAIN', 'Training'), ('ORDER', 'Order'), ('INCID', 'Incident'), ('FAIR', 'Trade fair'), ('FORUM', 'Forum')], default='MEET', max_length=5),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='importance',
            field=models.CharField(choices=[('4URG', 'Urgent'), ('3HI', 'High'), ('2MID', 'Medium'), ('1LOW', 'Low'), ('0FYI', 'Info')], default='1LOW', max_length=4),
        ),
    ]
