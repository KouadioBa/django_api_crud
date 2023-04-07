# Generated by Django 4.1.5 on 2023-04-05 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_user_the_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='the_client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_of_client', to='api.clients'),
        ),
    ]
