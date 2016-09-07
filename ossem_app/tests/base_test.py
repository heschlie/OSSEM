from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from ossem_app import models


class BaseTestCase(StaticLiveServerTestCase):

    def setup_lab(self):
        """
        This is used to setup a mock lab to test against

        :return:
        """
        # first we need a manufacturer
        self.mf = models.Manufacturer(
            name='ossem company'
        )
        self.mf.save()

        # next we need a model
        self.model_ = models.Model_(
            name='test-model',
            manufacturer=self.mf,
            size=2,
            shared_rack_unit=False,
            num_power_ports=1,
            estimated_kva_draw=1.5
        )
        self.model_.save()

        # next we need to create a Location, which requires a site at a minimum
        # but we should test all the fields
        self.site = models.Site(
            name='San Jose'
        )
        self.site.save()

        self.room = models.Room(
            name='Lab 2',
            site=self.site,
            size='2500sqft'
        )
        self.room.save()

        self.rack = models.Rack(
            name='12-15',
            total_rack_units=52,
            room=self.room,
            max_kva=14.2
        )
        self.rack.save()

        self.rack_b = models.Rack(
            name='12-16',
            total_rack_units=52,
            room=self.room,
            max_kva=14.2
        )
        self.rack_b.save()

        self.bench = models.Bench(
            name='Bench 5',
            room=self.room,
            max_kva=2.0
        )
        self.bench.save()

        self.shelf = models.Shelf(
            name='Dell Storage shelf',
            room=self.room,
            max_kva=1.0
        )
        self.shelf.save()

        # With all the above we can create a location
        self.location = models.Location(
            site=self.site,
            room=self.room,
            rack=self.rack,
            bench=self.bench,
            shelf=self.shelf
        )
        self.location.save()

        self.location_b = models.Location(
            site=self.site,
            room=self.room,
            rack=self.rack_b
        )
        self.location_b.save()

        # And now our device to test against
        self.device = models.Device(
            name='test-device-01',
            model=self.model_,
            location=self.location,
            rack_elevation=36
        )
        self.device.save()

        # Why not a list of other devices as well
        self.devs = [self.device]
        for i in range(10):
            dev = models.Device(
                name='test-mydev-{}'.format(i),
                model=self.model_,
                location=self.location,
                rack_elevation=i + 3
            )
            dev.save()
            self.devs.append(dev)
