# Generated by Django 2.0.5 on 2018-06-18 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oler', '0013_auto_20180617_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ridehistory',
            name='rider',
        ),
    ]