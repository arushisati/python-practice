class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(self.brand, self.model, "is starting...")


car1 = Car("Toyota", "Fortuner")
car1.start()
