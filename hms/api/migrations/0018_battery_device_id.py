# Generated by Django 2.2 on 2019-04-25 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20190425_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='battery',
            name='device_id',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
