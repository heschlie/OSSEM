# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossem_app', '0011_auto_20160722_0609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bench', models.ForeignKey(default=None, to='ossem_app.Bench')),
                ('rack', models.ForeignKey(default=None, to='ossem_app.Rack')),
                ('room', models.ForeignKey(default=None, to='ossem_app.Room')),
                ('shelf', models.ForeignKey(default=None, to='ossem_app.Shelf')),
                ('site', models.ForeignKey(default=None, to='ossem_app.Site')),
            ],
        ),
        migrations.AlterField(
            model_name='device',
            name='location',
            field=models.ForeignKey(to='ossem_app.Location', related_name='locations'),
        ),
    ]
