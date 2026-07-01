class Student:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print("Welcome", self.name)

s1 = Student("Arushi")
s1.welcome()
