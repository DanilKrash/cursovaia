# Generated by Django 4.1.6 on 2023-06-25 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='horse',
        ),
        migrations.RemoveField(
            model_name='order',
            name='trainer',
        ),
        migrations.AddField(
            model_name='order',
            name='horse',
            field=models.ManyToManyField(blank=True, to='horse.horse', verbose_name='Лошадь'),
        ),
        migrations.AddField(
            model_name='order',
            name='trainer',
            field=models.ManyToManyField(blank=True, to='horse.trainer', verbose_name='Тренер'),
        ),
    ]
