class Animal:
    def sound(self):
        print("Animals make sounds.")


class Dog(Animal):
    def sound(self):
        print("Dog says: Bark Bark")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow Meow")


d = Dog()
c = Cat()

d.sound()
c.sound()
