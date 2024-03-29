# Generated by Django 3.0.6 on 2020-08-09 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=45)),
                ('hierarchy', models.CharField(max_length=45)),
                ('img_url', models.CharField(max_length=255)),
                ('product_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.ProductGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=45)),
                ('turnover_class', models.CharField(max_length=45)),
                ('value', models.IntegerField()),
                ('product_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.ProductGroup')),
            ],
            options={
                'unique_together': {('status', 'turnover_class', 'product_group')},
            },
        ),
    ]
