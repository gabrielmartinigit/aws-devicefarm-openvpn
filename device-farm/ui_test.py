from uiautomator import Device
from time import sleep

sleep(3)
device = Device()

device(text="Settings").click()