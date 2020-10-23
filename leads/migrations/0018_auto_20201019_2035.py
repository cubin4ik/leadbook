# Generated by Django 3.0.6 on 2020-10-19 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0017_auto_20201019_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(choices=[('UNW', 'Неизвестно'), ('CEO', 'Генеральный директор'), ('EXD', 'Исполнительный директор'), ('DPD', 'Заместитель директора'), ('SAD', 'Директор по продажам'), ('HDP', 'Руководитель отдела'), ('ENG', 'Инженер'), ('EXP', 'Эксперт'), ('PUR', 'Специалист закупки'), ('PRG', 'Программист'), ('SAL', 'Продавец'), ('KAM', 'Ключевой менеджер по работе с Bosch'), ('MAN', 'Менеджер по работе с партнерами')], default='UNW', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='type',
            field=models.CharField(choices=[('MAIN', 'main'), ('MOB', 'mobile'), ('WRK', 'work'), ('PRS', 'personal')], default='MAIN', max_length=255),
        ),
    ]