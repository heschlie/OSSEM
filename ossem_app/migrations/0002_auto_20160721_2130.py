# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossem_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(default='default_name', max_length=240),
        ),
        migrations.AddField(
            model_name='model_',
            name='name',
            field=models.CharField(default='default_name', max_length=240),
        ),
        migrations.AddField(
            model_name='model_',
            name='parent',
            field=models.ForeignKey(null=True, related_name='children', to='ossem_app.Manufacturer'),
        ),
    ]
