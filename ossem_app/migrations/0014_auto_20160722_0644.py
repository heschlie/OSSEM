# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossem_app', '0013_auto_20160722_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='location',
            field=models.ForeignKey(related_name='devices', to='ossem_app.Location'),
        ),
    ]
