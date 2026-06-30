class Light:
    def __init__(self):
        self.status = "OFF"

    def turn_on(self):
        self.status = "ON"
        print(self.status)

l = Light()
l.turn_on()
