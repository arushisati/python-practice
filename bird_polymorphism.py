# bird_polymorphism.py

class Bird:
    def fly(self):
        print("Bird flies")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies high")

class Eagle(Bird):
    def fly(self):
        print("Eagle soars in the sky")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

birds = [Sparrow(), Eagle(), Penguin()]

for bird in birds:
    bird.fly()
