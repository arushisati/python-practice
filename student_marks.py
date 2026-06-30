class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        print(self.name)
        print("Marks:", self.marks)

s = Student("Arushi", 95)
s.result()
