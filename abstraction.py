# Abstraction Example

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Dog Barks")

# Object
d = Dog()

# Calling method
d.sound()
