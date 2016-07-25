from django.test import TestCase
from ossem_app.models import *
from ossem_app.views import *


# Create your tests here.
class ModelTests(TestCase):

    def setup_lab(self):
        """
        This is used to setup a mock lab to test against
        :return:
        """
        # first we need a manufacturer
        self.mf = Manufacturer()
        self.mf.name = 'ossem company'
        self.mf.save()

        # next we need a model
        self.model_ = Model_()
        self.model_.manufacturer = self.mf
        self.model_.name = 'test-model'
        self.model_.size = 2
        self.model_.shared_rack_unit = False
        self.model_.num_power_ports = 1
        self.model_.estimated_kva_draw = 1.5
        self.model_.save()

        # next we need to create a Location, which requires a site at a minimum
        # but we should test all the fields
        self.site = Site(name='San Jose')
        self.site.save()

        self.room = Room()
        self.room.name = 'Lab 2'
        self.room.site = self.site
        self.room.size = '2500sqft'
        self.room.save()

        self.rack = Rack()
        self.rack.name = '12-15'
        self.rack.units = 52
        self.rack.room = self.room
        self.rack.max_kva = 14.2
        self.rack.save()

        self.bench = Bench()
        self.bench.name = 'Bench 5'
        self.bench.room = self.room
        self.bench.max_kva = 2.0
        self.bench.save()

        self.shelf = Shelf()
        self.shelf.name = 'Dell storage shelf'
        self.shelf.room = self.room
        self.shelf.max_kva = 1.0
        self.shelf.save()

        # With all the above we can create a location
        self.location = Location()
        self.location.site = self.site
        self.location.room = self.room
        self.location.rack = self.rack
        self.location.bench = self.bench
        self.location.shelf = self.shelf
        self.location.save()

        # And now our device to test against
        self.device = Device()
        self.device.name = 'test-device-01'
        self.device.model = self.model_
        self.device.location = self.location
        self.device.rack_elevation = 36
        self.device.save()

        # Why not a list of other devices as well
        self.devs = [self.device]
        for i in range(10):
            dev = Device(
                name='test-mydev-{}'.format(i),
                model=self.model_,
                location=self.location,
                rack_elevation=i + 3
            )
            dev.save()
            self.devs.append(dev)

    def setUp(self):
        self.setup_lab()

    def test_site(self):
        saved_site = Site.objects.first()

        # Verify we see all of the other location related objects from here
        self.assertEqual(saved_site.number_of_rooms, 1)
        self.assertEqual(saved_site.number_of_racks, 1)
        self.assertEqual(saved_site.number_of_benches, 1)
        self.assertEqual(saved_site.number_of_shelves, 1)
        self.assertEqual(str(saved_site), str(self.site))

        self.assertEqual(saved_site.number_of_devices, len(self.devs))
        for dev in self.devs:
            saved_dev = Device.objects.get(name=dev.name)
            self.assertEqual(saved_dev, dev)

        self.assertIn(self.devs[0], saved_site.devices)

    def test_room(self):
        saved_room = Room.objects.first()

        self.assertIn(self.devs[0], saved_room.devices)
        self.assertGreater(saved_room.number_of_devices, 0)
        self.assertEqual(str(saved_room), str(self.room))

    def test_bench(self):
        saved_bench = Bench.objects.first()

        self.assertIn(self.devs[0], saved_bench.devices)

    def test_shelf(self):
        saved_shelf = Shelf.objects.first()

        self.assertIn(self.devs[0], saved_shelf.devices)

    def test_rack(self):
        saved_rack = Rack.objects.first()

        self.assertEqual(saved_rack, self.rack)
        self.assertEqual(str(saved_rack), str(self.rack))
        self.assertGreater(saved_rack.number_of_devices, 0)
        self.assertGreater(saved_rack.estimated_power_draw, 1)
        self.assertLess(saved_rack.estimated_free_kva, saved_rack.max_kva)
        self.assertLess(saved_rack.available_rack_units,
                        saved_rack.total_rack_units)
        self.assertIn(self.devs[0], saved_rack.devices)

    def test_location(self):
        # verify we can look up the location on out names
        # This should be done first when creating a new location to verify that
        # we are not creating new locations when not necessary
        saved_location = Location.objects.get(site__name=self.site.name,
                                              room__name=self.room.name,
                                              rack__name=self.rack.name,
                                              bench__name=self.bench.name,
                                              shelf__name=self.shelf.name)

        self.assertEqual(self.location, saved_location)

    def test_manufacturer(self):
        saved_mf = Manufacturer.objects.first()

        self.assertEqual(self.mf, saved_mf)
        self.assertEqual(str(saved_mf), str(self.mf))

    def test_model_(self):
        saved_model = Model_.objects.first()

        self.assertEqual(self.model_, saved_model)
        self.assertEqual(str(saved_model), str(self.model_))
        self.assertEqual(saved_model.size, self.model_.size)
        self.assertEqual(saved_model.shared_rack_unit,
                         self.model_.shared_rack_unit)
        self.assertEqual(saved_model.num_power_ports,
                         self.model_.num_power_ports)

    def test_device(self):
        saved_device = Device.objects.first()

        self.assertEqual(self.device, saved_device)
        self.assertEqual(str(saved_device), str(self.device))
        self.assertEqual(saved_device.model, self.device.model)
        self.assertEqual(saved_device.location, self.device.location)
        self.assertEqual(saved_device.rack_elevation,
                         self.device.rack_elevation)
