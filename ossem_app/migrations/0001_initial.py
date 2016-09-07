# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bench',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=240, default='')),
                ('max_kva', models.FloatField(default=0.0)),
                ('size', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=240, default='default_name')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('rack_elevation', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bench', models.ForeignKey(to='ossem_app.Bench', blank=True, related_name='locations', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=240, default='default_name')),
            ],
        ),
        migrations.CreateModel(
            name='Model_',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=240, default='default_name')),
                ('size', models.IntegerField(default=0)),
                ('shared_rack_unit', models.BooleanField(default=False)),
                ('num_power_ports', models.IntegerField(default=0)),
                ('estimated_kva_draw', models.FloatField(default=0.0)),
                ('manufacturer', models.ForeignKey(to='ossem_app.Manufacturer', null=True, related_name='models')),
            ],
            options={
                'ordering': ['manufacturer', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=240, default='')),
                ('max_kva', models.FloatField(default=0.0)),
                ('total_rack_units', models.IntegerField(default=42)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=240, default='')),
                ('size', models.CharField(max_length=80, default='0')),
            ],
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=240, default='')),
                ('max_kva', models.FloatField(default=0.0)),
                ('number_of_shelves', models.IntegerField(default=0)),
                ('room', models.ForeignKey(to='ossem_app.Room', default=None, related_name='shelves')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=240, default='')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='site',
            field=models.ForeignKey(to='ossem_app.Site', default=None, related_name='rooms'),
        ),
        migrations.AddField(
            model_name='rack',
            name='room',
            field=models.ForeignKey(to='ossem_app.Room', default=None, related_name='racks'),
        ),
        migrations.AddField(
            model_name='location',
            name='rack',
            field=models.ForeignKey(to='ossem_app.Rack', blank=True, related_name='locations', null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='room',
            field=models.ForeignKey(to='ossem_app.Room', blank=True, related_name='locations', null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='shelf',
            field=models.ForeignKey(to='ossem_app.Shelf', blank=True, related_name='locations', null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='site',
            field=models.ForeignKey(to='ossem_app.Site', blank=True, related_name='locations', null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='location',
            field=models.ForeignKey(to='ossem_app.Location', related_name='devices'),
        ),
        migrations.AddField(
            model_name='device',
            name='model',
            field=models.ForeignKey(to='ossem_app.Model_', default=None, related_name='devices'),
        ),
        migrations.AddField(
            model_name='device',
            name='parent',
            field=models.ForeignKey(to='ossem_app.Device', blank=True, related_name='children', null=True),
        ),
        migrations.AddField(
            model_name='bench',
            name='room',
            field=models.ForeignKey(to='ossem_app.Room', default=None, related_name='benches'),
        ),
    ]
