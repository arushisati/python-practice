# device_polymorphism.py

class Device:
    def power_on(self):
        print("Device is ON")

class Laptop(Device):
    def power_on(self):
        print("Laptop Booting...")

class Mobile(Device):
    def power_on(self):
        print("Mobile Starting...")

class Tablet(Device):
    def power_on(self):
        print("Tablet Turning On...")

devices = [Laptop(), Mobile(), Tablet()]

for device in devices:
    device.power_on()
