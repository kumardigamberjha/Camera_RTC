# Generated by Django 4.0.6 on 2022-08-03 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websocketspy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancemodel',
            name='late',
        ),
        migrations.RemoveField(
            model_name='attendancemodel',
            name='salary_deduct',
        ),
    ]
