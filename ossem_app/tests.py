from django.test import TestCase
from ossem_app.models import *

# Create your tests here.
class ModelTests(TestCase):

    def test_manufacturer_model_location_device_models(self):
        # first we need a manufacturer
        mf = Manufacturer()
        mf.name = 'ossem company'
        mf.save()

        # next we need a model
        model = Model_()
        model.manufacturer = mf
        model.name = 'test-model'
        model.size = 2
        model.shared_rack_unit = False
        model.num_power_ports = 1
        model.estimated_kva_draw = 1.5
        model.save()

        # next we need to create a Location, which requires a site at a minimum,
        # but we should test all the fields
        site = Site(name='San Jose')
        site.save()

        room = Room()
        room.name = 'Lab 2'
        room.site = site
        room.size = '2500sqft'
        room.save()

        rack = Rack()
        rack.name = '12-15'
        rack.units = 52
        rack.room = room
        rack.max_kva = 14.2
        rack.save()

        bench = Bench()
        bench.name = 'Bench 5'
        bench.room = room
        bench.max_kva = 2.0
        bench.save()

        shelf = Shelf()
        shelf.name = 'Dell storage shelf'
        shelf.room = room
        shelf.max_kva = 1.0
        shelf.save()

        location = Location()
        location.site = site
        location.room = room
        location.rack = rack
        location.bench = bench
        location.shelf = shelf
        location.save()

        # Let's test the calculated fields here
        # We only need to test the location class as it pulls from the other
        # calculated properties of the others
        saved_site = Site.objects.first()
        self.assertEqual(saved_site.number_of_rooms, 1)
        self.assertEqual(saved_site.number_of_racks, 1)
        self.assertEqual(saved_site.number_of_benches, 1)
        self.assertEqual(saved_site.number_of_shelves, 1)

        # finally we can create a device
        device = Device()
        device.name = 'test-device-01'
        device.model = model
        device.location = location
        device.rack_elevation = 36
        device.save()

        # let's retrieve the Manufacturer from the DB and check all was saved
        saved_mf = Manufacturer.objects.first()
        self.assertEqual(mf, saved_mf)
        self.assertEqual(saved_mf.name, mf.name)

        saved_model = saved_mf.models.all()[0]
        self.assertEqual(model, saved_model)
        self.assertEqual(saved_model.name, model.name)
        self.assertEqual(saved_model.size, model.size)
        self.assertEqual(saved_model.shared_rack_unit, model.shared_rack_unit)
        self.assertEqual(saved_model.num_power_ports, model.num_power_ports)

        saved_device = saved_model.devices.all()[0]
        self.assertEqual(device, saved_device)
        self.assertEqual(saved_device.name, device.name)
        self.assertEqual(saved_device.model, device.model)
        self.assertEqual(saved_device.location, device.location)
        self.assertEqual(saved_device.rack_elevation, device.rack_elevation)

        # Now that we have a device let's check some more of the calculated
        # methods
        saved_rack = Rack.objects.first()
        self.assertGreater(saved_rack.estimated_power_draw, 1)
        self.assertLess(saved_rack.estimated_free_kva, saved_rack.max_kva)
        self.assertLess(saved_rack.available_rack_units, saved_rack.total_rack_units)
