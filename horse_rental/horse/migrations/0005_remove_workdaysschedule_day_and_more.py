# Generated by Django 4.1.7 on 2024-06-22 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0004_days_workschedule_workdaysschedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workdaysschedule',
            name='day',
        ),
        migrations.RemoveField(
            model_name='workdaysschedule',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='workdaysschedule',
            name='trainer',
        ),
        migrations.DeleteModel(
            name='Days',
        ),
        migrations.DeleteModel(
            name='WorkDaysSchedule',
        ),
        migrations.DeleteModel(
            name='WorkSchedule',
        ),
    ]
