class Flower:
    def __init__(self, name):
        self.name = name

    def bloom(self):
        print(self.name, "is blooming.")


f = Flower("Rose")
f.bloom()
