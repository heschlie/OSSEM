from ossem_app.tests.base_test import BaseTestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BaseFunctionalTest(BaseTestCase):

    def setUp(self):
        self.setup_lab()
        caps = DesiredCapabilities.FIREFOX
        caps['marionette'] = True
        self.browser = webdriver.Firefox(capabilities=caps)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
