# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossem_app', '0003_auto_20160721_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='model',
            field=models.ForeignKey(default=None, to='ossem_app.Model_', related_name='devices'),
        ),
        migrations.AddField(
            model_name='device',
            name='name',
            field=models.CharField(max_length=240, default='default_name'),
        ),
    ]
