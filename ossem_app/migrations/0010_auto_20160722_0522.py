# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossem_app', '0009_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=240, default='')),
                ('size', models.CharField(max_length=80, default='0')),
            ],
        ),
        migrations.AddField(
            model_name='site',
            name='name',
            field=models.CharField(max_length=240, default=''),
        ),
        migrations.AddField(
            model_name='room',
            name='site',
            field=models.ForeignKey(to='ossem_app.Site', related_name='rooms', default=None),
        ),
    ]
