# Generated by Django 4.1.7 on 2024-06-22 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0005_remove_workdaysschedule_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='time',
            field=models.IntegerField(verbose_name='Время оказания услуги'),
        ),
    ]
