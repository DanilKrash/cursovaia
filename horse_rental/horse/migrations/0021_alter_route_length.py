# Generated by Django 4.1.7 on 2024-05-23 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0020_remove_horse_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='length',
            field=models.IntegerField(max_length=50, verbose_name='Протяжённость'),
        ),
    ]
