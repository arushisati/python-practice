# Common Method Polymorphism

class Bird:
    def move(self):
        print("Bird flies.")

class Fish:
    def move(self):
        print("Fish swims.")

class Snake:
    def move(self):
        print("Snake crawls.")

animals = [Bird(), Fish(), Snake()]

for animal in animals:
    animal.move()
