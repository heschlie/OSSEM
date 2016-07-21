# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossem_app', '0005_auto_20160721_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_',
            name='num_power_ports',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='model_',
            name='shared_rack_unit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='model_',
            name='size',
            field=models.IntegerField(default=0),
        ),
    ]
