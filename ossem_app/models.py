from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=240, default='default_name')

    def __str__(self):
        return self.name


class Model_(models.Model):
    name = models.CharField(max_length=240, default='default_name')
    manufacturer = models.ForeignKey(Manufacturer, related_name='models', null=True)
    size = models.IntegerField(default=0)
    shared_rack_unit = models.BooleanField(default=False)
    num_power_ports = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(max_length=240, default='default_name')
    model = models.ForeignKey(Model_, related_name='devices', default=None)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Device(Resource):
    location = models.CharField(max_length=120, default=None)
    rack_elevation = models.IntegerField(default=0)
