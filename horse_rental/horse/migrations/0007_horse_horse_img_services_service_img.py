# Generated by Django 4.1.6 on 2023-05-09 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0006_rename_service_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='horse',
            name='horse_img',
            field=models.ImageField(default=1, upload_to='%Y/%m/%d/', verbose_name='Фото'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='service_img',
            field=models.ImageField(default=1, upload_to='%Y/%m/%d/', verbose_name='Фото'),
            preserve_default=False,
        ),
    ]