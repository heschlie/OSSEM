# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossem_app', '0012_auto_20160722_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='bench',
            field=models.ForeignKey(default=None, to='ossem_app.Bench', related_name='locations'),
        ),
        migrations.AlterField(
            model_name='location',
            name='rack',
            field=models.ForeignKey(default=None, to='ossem_app.Rack', related_name='locations'),
        ),
        migrations.AlterField(
            model_name='location',
            name='room',
            field=models.ForeignKey(default=None, to='ossem_app.Room', related_name='locations'),
        ),
        migrations.AlterField(
            model_name='location',
            name='shelf',
            field=models.ForeignKey(default=None, to='ossem_app.Shelf', related_name='locations'),
        ),
        migrations.AlterField(
            model_name='location',
            name='site',
            field=models.ForeignKey(default=None, to='ossem_app.Site', related_name='locations'),
        ),
    ]
