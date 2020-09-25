# Generated by Django 3.0.6 on 2020-09-17 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0016_auto_20200917_1226'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reminder',
            options={'ordering': ['-importance', 'due_time']},
        ),
        migrations.AddField(
            model_name='reminder',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Event'),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='importance',
            field=models.CharField(choices=[('4URG', 'Urgent'), ('3HI', 'High'), ('2MID', 'Medium'), ('1LOW', 'Low'), ('0FYI', 'For your information')], default='1LOW', max_length=4),
        ),
    ]
