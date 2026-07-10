# college_class.py

class College:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display(self):
        print("College Name :", self.name)
        print("Course       :", self.course)


# Main Program
college = College("ABC College", "B.Sc AIML")
college.display()
