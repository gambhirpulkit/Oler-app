# Generated by Django 2.0.5 on 2018-06-14 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oler', '0002_riderhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riderhistory',
            name='ride_type',
            field=models.IntegerField(choices=[(1, 'share'), (2, 'mini_go')], default=2),
        ),
    ]
