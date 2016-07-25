# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossem_app', '0015_device_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shelf',
            old_name='number_of_shlelves',
            new_name='number_of_shelves',
        ),
    ]
