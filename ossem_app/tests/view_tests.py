from django.test import TestCase

from .base_test import BaseTestCase
from ossem_app import views


class DeviceView(BaseTestCase):

    def setUp(self):
        self.setup_lab()

    def test_device_list_view(self):
        pass

    def test_device_details_view(self):
        pass
