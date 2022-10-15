class Device:
    def __init__(self, name, storage, size):
        self.__name = name
        self.storage = storage
        self.size = size

    def detail(self):
        print(f"This is a {self.__name} device with  {self.storage}GB storage \n and a {self.size}inch screensize")


class Phone(Device):
    def __init__(self, storage, size):
        Device. __init__(self, storage, size)
    androidversion = 10
    broadband = "4G"

    def print_it(self):
        Device.detail(self)
        print(f"this phone also of version{Phone.androidversion} and speed of {Phone.broadband}")


purchase = Device("Samsung", 48, "10-50")
purchase.detail()

siimu = Phone("Samy", 64, "20-60")
siimu.print_it()


