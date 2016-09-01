from django.db import models


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=240, default='default_name')

    def __str__(self):
        return self.name


class Model_(models.Model):
    name = models.CharField(max_length=240, default='default_name')
    manufacturer = models.ForeignKey(Manufacturer, related_name='models',
                                     null=True)
    size = models.IntegerField(default=0)
    shared_rack_unit = models.BooleanField(default=False)
    num_power_ports = models.IntegerField(default=0)
    estimated_kva_draw = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(max_length=240, default='default_name')
    model = models.ForeignKey(Model_, related_name='devices', default=None)
    parent = models.ForeignKey('self', related_name='children', null=True,
                               blank=True)

    @property
    def manufacturer(self):
        return self.model.manufacturer

    @property
    def size(self):
        return self.model.size

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Device(Resource):
    location = models.ForeignKey('Location', related_name='devices')
    rack_elevation = models.IntegerField(default=0)


class Site(models.Model):
    name = models.CharField(max_length=240, default='')

    @property
    def number_of_rooms(self):
        return self.rooms.count()

    @property
    def number_of_racks(self):
        num_racks = 0
        for room in self.rooms.all():
            num_racks += room.number_of_racks

        return num_racks

    @property
    def number_of_benches(self):
        num_bench = 0
        for room in self.rooms.all():
            num_bench += room.number_of_benches

        return num_bench

    @property
    def number_of_shelves(self):
        num_shelf = 0
        for room in self.rooms.all():
            num_shelf += room.number_of_shelves

        return num_shelf

    @property
    def number_of_devices(self):
        num_device = 0
        for location in self.locations.all():
            num_device += location.devices.count()

        return num_device

    @property
    def devices(self):
        devs = []
        for room in self.rooms.all():
            devs.extend(room.devices)
        return devs

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=240, default='')
    site = models.ForeignKey(Site, related_name='rooms', default=None)
    size = models.CharField(max_length=80, default='0')

    @property
    def number_of_racks(self):
        return self.racks.count()

    @property
    def number_of_benches(self):
        return self.benches.count()

    @property
    def number_of_shelves(self):
        return self.shelves.count()

    @property
    def number_of_devices(self):
        num_device = 0
        for location in self.locations.all():
            num_device += location.devices.count()

        return num_device

    @property
    def devices(self):
        devs = set()
        for location in self.locations.all():
            devs.update(location.devices.all())

        return devs

    def __str__(self):
        return self.name


class DeviceContainer(models.Model):
    name = models.CharField(max_length=240, default='')
    max_kva = models.FloatField(default=0.0)

    @property
    def estimated_power_draw(self):
        kva = 0
        for location in self.locations.all():
            for device in location.devices.all():
                kva += device.model.estimated_kva_draw

        return kva

    @property
    def estimated_free_kva(self):
        return self.max_kva - self.estimated_power_draw

    @property
    def number_of_devices(self):
        num_device = 0
        for location in self.locations.all():
            num_device += location.devices.count()

        return num_device

    @property
    def devices(self):
        devices = set()
        for location in self.locations.all():
            devices.update(location.devices.all())

        return devices

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Rack(DeviceContainer):
    total_rack_units = models.IntegerField(default=42)
    room = models.ForeignKey(Room, related_name='racks', default=None)

    @property
    def occupied_space(self):
        space = 0
        for location in self.locations.all():
            for device in location.devices.all():
                space += device.model.size

        return space

    @property
    def available_rack_units(self):
        return self.total_rack_units - self.occupied_space


class Bench(DeviceContainer):
    size = models.IntegerField(default=0)
    room = models.ForeignKey(Room, related_name='benches', default=None)


class Shelf(DeviceContainer):
    number_of_shelves = models.IntegerField(default=0)
    room = models.ForeignKey(Room, related_name='shelves', default=None)


class Location(models.Model):
    site = models.ForeignKey(Site, related_name='locations', null=True,
                             blank=True)
    room = models.ForeignKey(Room, related_name='locations', null=True,
                             blank=True)
    rack = models.ForeignKey(Rack, related_name='locations', null=True,
                             blank=True)
    bench = models.ForeignKey(Bench, related_name='locations', null=True,
                              blank=True)
    shelf = models.ForeignKey(Shelf, related_name='locations', null=True,
                              blank=True)

    def __str__(self):
        name = [self.site.name]
        if self.room:
            name.append(self.room.name)
        if self.bench:
            name.append(self.bench.name)
        if self.rack:
            name.append(self.rack.name)
        if self.shelf:
            name.append(self.shelf.name)

        return '->'.join(name)
