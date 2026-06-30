class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def introduce(self):
        print(f"My name is {self.name}.")
        print(f"I live in {self.city}.")

p = Person("Arushi", "Delhi")
p.introduce()
