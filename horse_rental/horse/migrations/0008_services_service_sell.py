# Generated by Django 4.1.6 on 2023-05-09 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0007_horse_horse_img_services_service_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='service_sell',
            field=models.CharField(default=1, max_length=50, verbose_name='Цена'),
            preserve_default=False,
        ),
    ]
