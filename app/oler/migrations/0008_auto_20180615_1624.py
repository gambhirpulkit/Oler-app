# Generated by Django 2.0.5 on 2018-06-15 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oler', '0007_auto_20180615_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=False, verbose_name='Driver availability')),
                ('car_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='is_driver',
            field=models.BooleanField(default=False, verbose_name='Driver'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_rider',
            field=models.BooleanField(default=False, verbose_name='Rider'),
        ),
        migrations.AddField(
            model_name='driverprofile',
            name='driver',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
