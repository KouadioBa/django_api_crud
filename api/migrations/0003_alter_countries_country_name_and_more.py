# Generated by Django 4.1.5 on 2023-04-13 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_number_of_clients_countries_numbers_of_clients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countries',
            name='country_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='country_prefixe',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
