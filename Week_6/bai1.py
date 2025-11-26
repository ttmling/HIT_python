class Manufacterer:
    def __init__(self, identity, location):
        self.identity = identity
        self.location = location
    def describe(self):
        print(f"Identity: {self.identity} - Location: {self.location}")

class Device:
    def __init__(self, name, price, identity, location):
        self.name = name
        self.price = price
        Manufacterer.__init__(self, identity, location)
    def describe(self):
        print(f"Name: {self.name} - Price: {self.price}")
        Manufacterer.describe(self)

device1 = Device("mouse", 2500, 9725, "Vietnam")
device1.describe()
device2 = Device("monitor", 12.5, 11, "Gẻmany")
device2.describe()