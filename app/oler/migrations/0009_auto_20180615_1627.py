# Generated by Django 2.0.5 on 2018-06-15 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oler', '0008_auto_20180615_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverprofile',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ridehistory',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ridehistory',
            name='rider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rider', to=settings.AUTH_USER_MODEL),
        ),
    ]
