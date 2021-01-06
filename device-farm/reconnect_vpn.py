from uiautomator import Device
from subprocess import call
from time import sleep

call(["adb", "shell", "am", "start", "-W", "-n", "net.openvpn.openvpn/net.openvpn.unified.MainActivity"])

sleep(3)
device = Device()
  
if device(description='connect').exists:
    device(description='connect').click()
    print("Started the VPN!")
else:
    print("VPN was already started!")