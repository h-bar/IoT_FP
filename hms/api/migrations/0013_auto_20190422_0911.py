# Generated by Django 2.2 on 2019-04-22 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20190419_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='amenities',
            name='locker_lights',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='amenities',
            name='locker_lights_p',
            field=models.FloatField(default=0),
        ),
    ]
