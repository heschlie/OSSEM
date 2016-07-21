# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossem_app', '0004_auto_20160721_2140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='model_',
            old_name='parent',
            new_name='manufacturer',
        ),
    ]
