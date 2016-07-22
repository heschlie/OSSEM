# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossem_app', '0010_auto_20160722_0522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bench',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(default='', max_length=240)),
                ('max_kva', models.FloatField(default=0.0)),
                ('size', models.IntegerField(default=0)),
                ('room', models.ForeignKey(related_name='benches', to='ossem_app.Room', default=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(default='', max_length=240)),
                ('max_kva', models.FloatField(default=0.0)),
                ('total_rack_units', models.IntegerField(default=42)),
                ('room', models.ForeignKey(related_name='racks', to='ossem_app.Room', default=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(default='', max_length=240)),
                ('max_kva', models.FloatField(default=0.0)),
                ('number_of_shlelves', models.IntegerField(default=0)),
                ('room', models.ForeignKey(related_name='shelves', to='ossem_app.Room', default=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='model_',
            name='estimated_kva_draw',
            field=models.FloatField(default=0.0),
        ),
    ]
