# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossem_app', '0014_auto_20160722_0644'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='parent',
            field=models.ForeignKey(related_name='children', to='ossem_app.Device', blank=True, null=True),
        ),
    ]
