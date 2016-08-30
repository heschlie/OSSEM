from ossem_app import models
from .base_test import BaseTestCase


# Create your tests here.
class ModelTests(BaseTestCase):

    def setUp(self):
        self.setup_lab()

    def test_site(self):
        saved_site = models.Site.objects.first()

        # Verify we see all of the other location related objects from here
        self.assertGreater(saved_site.number_of_rooms, 0)
        self.assertGreater(saved_site.number_of_racks, 0)
        self.assertGreater(saved_site.number_of_benches, 0)
        self.assertGreater(saved_site.number_of_shelves, 0)
        self.assertEqual(str(saved_site), str(self.site))

        self.assertEqual(saved_site.number_of_devices, len(self.devs))
        for dev in self.devs:
            saved_dev = models.Device.objects.get(name=dev.name)
            self.assertEqual(saved_dev, dev)

        self.assertIn(self.devs[0], saved_site.devices)

    def test_room(self):
        saved_room = models.Room.objects.first()

        self.assertIn(self.devs[0], saved_room.devices)
        self.assertGreater(saved_room.number_of_devices, 0)
        self.assertEqual(str(saved_room), str(self.room))

    def test_bench(self):
        saved_bench = models.Bench.objects.first()

        self.assertIn(self.devs[0], saved_bench.devices)

    def test_shelf(self):
        saved_shelf = models.Shelf.objects.first()

        self.assertIn(self.devs[0], saved_shelf.devices)

    def test_rack(self):
        saved_rack = models.Rack.objects.first()

        self.assertEqual(saved_rack, self.rack)
        self.assertEqual(str(saved_rack), str(self.rack))
        self.assertGreater(saved_rack.number_of_devices, 0)
        self.assertGreater(saved_rack.estimated_power_draw, 1)
        self.assertLess(saved_rack.estimated_free_kva, saved_rack.max_kva)
        self.assertLess(saved_rack.available_rack_units,
                        saved_rack.total_rack_units)
        self.assertIn(self.devs[0], saved_rack.devices)

    def test_location(self):
        # verify we can look up the location on our names
        # This should be done first when creating a new location to verify that
        # we are not creating new locations when not necessary
        saved_location = models.Location.objects.get(
            site__name=self.site.name,
            room__name=self.room.name,
            rack__name=self.rack.name,
            bench__name=self.bench.name,
            shelf__name=self.shelf.name
        )

        self.assertEqual(self.location, saved_location)
        self.assertEqual(str(self.location), str(saved_location))

        saved_location_b = models.Location.objects.get(
            site__name=self.site.name,
            room__name=self.room.name,
            rack__name=self.rack_b.name
        )

        self.assertEqual(self.location_b, saved_location_b)
        self.assertEqual(str(self.location_b), str(saved_location_b))

        self.assertNotEqual(saved_location_b, saved_location)

    def test_manufacturer(self):
        saved_mf = models.Manufacturer.objects.first()

        self.assertEqual(self.mf, saved_mf)
        self.assertEqual(str(saved_mf), str(self.mf))

    def test_model_(self):
        saved_model = models.Model_.objects.first()

        self.assertEqual(self.model_, saved_model)
        self.assertEqual(str(saved_model), str(self.model_))
        self.assertEqual(saved_model.size, self.model_.size)
        self.assertEqual(saved_model.shared_rack_unit,
                         self.model_.shared_rack_unit)
        self.assertEqual(saved_model.num_power_ports,
                         self.model_.num_power_ports)

    def test_device(self):
        saved_device = models.Device.objects.first()

        self.assertEqual(self.device, saved_device)
        self.assertEqual(str(saved_device), str(self.device))
        self.assertEqual(saved_device.model, self.device.model)
        self.assertEqual(saved_device.location, self.device.location)
        self.assertEqual(saved_device.rack_elevation,
                         self.device.rack_elevation)
