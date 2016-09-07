#!/usr/bin/env python3
import random

import os
import sys
import django


proj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + 'OSSEM'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OSSEM.settings')
sys.path.append(proj_path)
django.setup()

from ossem_app.models import (Manufacturer,
                              Model_,
                              Device,
                              Site,
                              Room,
                              Rack,
                              Bench,
                              Shelf,
                              Location)

# Let's create a site to store racks and equipment
site = Site.objects.create(name='Concord, CA')
room = Room.objects.create(name='L2', site=site, size='2500sqft')

# Let's create some racks to put devices in
for i in range(1, 10):
    for j in range(1, 15):
        # Our format here is row-rack, a common layout for datacenters
        name = '{}-{}'.format(i, j)
        rack = Rack.objects.create(name=name, max_kva=12.4, room=room)
        Location.objects.create(site=site, room=room, rack=rack)

# We should add a bench and shelf too
bench = Bench.objects.create(name='bench-1', max_kva=12.4, room=room)
Location.objects.create(site=site, room=room, bench=bench)

shelf = Shelf.objects.create(name='shelf-1', max_kva=12.4, room=room)
Location.objects.create(site=site, room=room, shelf=shelf)

# Setup a Manufacturer and Model to use
dell = Manufacturer.objects.create(name='Dell')
cisco = Manufacturer.objects.create(name='Cisco')
eric = Manufacturer.objects.create(name='Ericsson')

Model_.objects.create(name='R630', manufacturer=dell, size=1, num_power_ports=2,
                      estimated_kva_draw=0.6)
Model_.objects.create(name='R730', manufacturer=dell, size=2, num_power_ports=2,
                      estimated_kva_draw=0.6)
Model_.objects.create(name='S6000', manufacturer=dell, size=1,
                      num_power_ports=2, estimated_kva_draw=0.6)

Model_.objects.create(name='2900', manufacturer=cisco, size=1,
                      num_power_ports=1, estimated_kva_draw=0.4)
Model_.objects.create(name='6500', manufacturer=cisco, size=10,
                      num_power_ports=2, estimated_kva_draw=1.4)
Model_.objects.create(name='3600', manufacturer=cisco, size=1,
                      num_power_ports=1, estimated_kva_draw=0.4)

Model_.objects.create(name='SE1200', manufacturer=eric, size=12,
                      num_power_ports=2, estimated_kva_draw=2.6)
Model_.objects.create(name='SE600', manufacturer=eric, size=8,
                      num_power_ports=2, estimated_kva_draw=1.6)
Model_.objects.create(name='SSR8020', manufacturer=eric, size=38,
                      num_power_ports=10, estimated_kva_draw=10.0)

# Generate some devices to play with
locations = Location.objects.all()
models = Model_.objects.all()
for i in range(1, 101):
    name = 'ossem-testdev-{:02d}'.format(i)
    Device.objects.create(name=name,
                          model=random.choice(models),
                          location=random.choice(locations),
                          rack_elevation=random.randint(1, 42))
