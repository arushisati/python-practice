class Student:
    def __init__(self, fullname):
        self.name = fullname
        print("Adding a new name in database...")

s1 = Student("kran")
print(s1.name)
