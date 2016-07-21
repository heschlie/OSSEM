# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossem_app', '0006_auto_20160721_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='location',
            field=models.CharField(default=None, max_length=120),
        ),
    ]
