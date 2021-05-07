# Generated by Django 3.0.6 on 2021-04-20 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0027_company_partners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.CharField(choices=[('ACT_LOY', 'Active customer (loyal)'), ('ACT_DIS', 'Active customer (disloyal)'), ('POT_LOY', 'Potential customer (loyal)'), ('POT_CON', 'Potential customer (in contact)'), ('POT_UNK', 'Potential customer (not in contact)'), ('CMP_USF', 'Competitor (useless)'), ('CMP_USL', 'Competitor (useful)'), ('UNKNOWN', 'Unknown'), ('BLOCKED', 'Blocked')], default='UNKNOWN', max_length=7),
        ),
    ]
