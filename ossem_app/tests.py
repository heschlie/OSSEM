from django.test import TestCase
from ossem_app.models import Manufacturer, Model_, Device

# Create your tests here.
class ModelTests(TestCase):

    def test_manufacturer_model_device_models(self):
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
        model.save()

        # finally we can create a device
        device = Device()
        device.name = 'test-device-01'
        device.model = model
        device.location = '01-12'
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
