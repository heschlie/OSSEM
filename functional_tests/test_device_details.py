from .base_test import BaseFunctionalTest
from time import sleep


class DeviceDetailsTest(BaseFunctionalTest):

    def test_table_exists(self):
        url = self.live_server_url + '/ossem/{}/'.format(self.device.id)
        self.browser.get(url)
        sleep(5)
