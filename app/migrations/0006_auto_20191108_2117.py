# Generated by Django 2.2.5 on 2019-11-08 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20191108_2115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='datetime',
            new_name='date_time',
        ),
    ]
