# Generated by Django 2.2 on 2019-04-19 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_amenities'),
    ]

    operations = [
        migrations.CreateModel(
            name='kiosk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField(default=0)),
                ('timestamp', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='amenities',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='amenities',
            name='blender',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='amenities',
            name='blender_p',
            field=models.FloatField(default=False),
        ),
        migrations.AddField(
            model_name='amenities',
            name='coffee_machine',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='amenities',
            name='coffee_machine_p',
            field=models.FloatField(default=False),
        ),
        migrations.AddField(
            model_name='amenities',
            name='kiosk_lights',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='amenities',
            name='kiosk_lights_p',
            field=models.FloatField(default=False),
        ),
        migrations.AddField(
            model_name='amenities',
            name='mini_frige',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='amenities',
            name='mini_frige_p',
            field=models.FloatField(default=False),
        ),
        migrations.AddField(
            model_name='amenities',
            name='tv',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='amenities',
            name='tv_p',
            field=models.FloatField(default=False),
        ),
    ]
