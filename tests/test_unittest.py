import os
import unittest
from appium import webdriver
from time import sleep


class DeviceFarmAppiumWebTests(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        self.driver = webdriver.Remote(
            'http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_devicefarm(self):
        self.driver.get(
            'http://10.192.21.35')
        sleep(5)
        screenshot_folder = os.getenv('SCREENSHOT_PATH', '/tmp')
        self.driver.save_screenshot(screenshot_folder + '/devicefarm.png')
        sleep(5)

# Start of script
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DeviceFarmAppiumWebTests)
    unittest.TextTestRunner(verbosity=2).run(suite)