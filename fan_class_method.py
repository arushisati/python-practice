class Fan:
    def __init__(self, brand):
        self.brand = brand

    def turn_on(self):
        print(self.brand, "Fan is ON")


f = Fan("Usha")
f.turn_on()
