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
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


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
        for room in self.rooms.all():
            num_device += room.number_of_devices

        return num_device


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
        for rack in self.racks.all():
            num_device += rack.number_of_devices

        for bench in self.benches.all():
            num_device += bench.number_of_devices

        for shelf in self.shelves.all():
            num_device += shelf.number_of_devices

        return num_device


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
    def get_devices(self):
        devices = []
        for location in self.locations.all():
            devices.extend(location.devices.all())

        return devices

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
    number_of_shlelves = models.IntegerField(default=0)
    room = models.ForeignKey(Room, related_name='shelves', default=None)


class Location(models.Model):
    site = models.ForeignKey(Site, related_name='locations', default=None)
    room = models.ForeignKey(Room, related_name='locations', default=None)
    rack = models.ForeignKey(Rack, related_name='locations', default=None)
    bench = models.ForeignKey(Bench, related_name='locations', default=None)
    shelf = models.ForeignKey(Shelf, related_name='locations', default=None)


class Device(Resource):
    location = models.ForeignKey(Location, related_name='devices')
    rack_elevation = models.IntegerField(default=0)
