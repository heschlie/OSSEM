# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossem_app', '0002_auto_20160721_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_',
            name='parent',
            field=models.ForeignKey(to='ossem_app.Manufacturer', related_name='models', null=True),
        ),
    ]
