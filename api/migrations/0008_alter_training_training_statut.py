# Generated by Django 4.1.5 on 2023-04-14 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_training_training_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='training_statut',
            field=models.IntegerField(default=0),
        ),
    ]