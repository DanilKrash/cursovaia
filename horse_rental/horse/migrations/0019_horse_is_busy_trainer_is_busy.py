# Generated by Django 4.1.7 on 2024-05-17 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0018_alter_services_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='horse',
            name='is_busy',
            field=models.BooleanField(default=False, verbose_name='Занята'),
        ),
        migrations.AddField(
            model_name='trainer',
            name='is_busy',
            field=models.BooleanField(default=False, verbose_name='Занят'),
        ),
    ]