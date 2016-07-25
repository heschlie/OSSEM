# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossem_app', '0016_auto_20160725_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='bench',
            field=models.ForeignKey(to='ossem_app.Bench', null=True, related_name='locations', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='rack',
            field=models.ForeignKey(to='ossem_app.Rack', null=True, related_name='locations', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='room',
            field=models.ForeignKey(to='ossem_app.Room', null=True, related_name='locations', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='shelf',
            field=models.ForeignKey(to='ossem_app.Shelf', null=True, related_name='locations', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='site',
            field=models.ForeignKey(to='ossem_app.Site', null=True, related_name='locations', blank=True),
        ),
    ]
