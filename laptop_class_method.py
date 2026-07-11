class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def details(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram, "GB")


lap = Laptop("HP", 16)
lap.details()
