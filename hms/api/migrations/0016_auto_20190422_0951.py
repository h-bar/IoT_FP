# Generated by Django 2.2 on 2019-04-22 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20190422_0927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amenities',
            old_name='mini_frige',
            new_name='mini_fridge',
        ),
        migrations.RenameField(
            model_name='amenities',
            old_name='mini_frige_p',
            new_name='mini_fridge_p',
        ),
    ]
