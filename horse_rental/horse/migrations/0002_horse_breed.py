# Generated by Django 4.1.6 on 2023-05-07 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='horse',
            name='breed',
            field=models.CharField(default=1, max_length=30, verbose_name='Порода'),
            preserve_default=False,
        ),
    ]
