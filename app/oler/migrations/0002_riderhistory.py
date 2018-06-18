# Generated by Django 2.0.5 on 2018-06-14 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiderHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ride_type', models.IntegerField(choices=[(1, 'share'), (2, 'mingo')], default=2)),
                ('ride_state', models.IntegerField(choices=[(1, 'accepted'), (2, 'ongoing'), (3, 'completed')], default=0)),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='driver', to=settings.AUTH_USER_MODEL)),
                ('rider', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rider', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]