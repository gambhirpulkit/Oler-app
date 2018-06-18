# Generated by Django 2.0.5 on 2018-06-15 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oler', '0003_auto_20180614_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riderhistory',
            name='ride_state',
            field=models.IntegerField(choices=[(1, 'requested'), (2, 'accepted'), (3, 'ongoing'), (4, 'completed'), (5, 'rejected')], default=0),
        ),
    ]
