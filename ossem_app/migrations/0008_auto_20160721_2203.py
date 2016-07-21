# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossem_app', '0007_device_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='rack_elevation',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='model_',
            name='num_power_ports',
            field=models.IntegerField(default=0),
        ),
    ]
