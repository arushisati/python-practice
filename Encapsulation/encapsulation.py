# Creating a class named Student
class Student:

    # Constructor to initialize object
    def __init__(self, name, marks):

        # Public attribute (can be accessed from anywhere)
        self.name = name

        # Private attribute (cannot be accessed directly)
        self.__marks = marks

    # Getter method to access private data
    def get_marks(self):
        return self.__marks

    # Setter method to modify private data
    def set_marks(self, marks):

        # Validation
        if marks >= 0:
            self.__marks = marks
        else:
            print("Marks cannot be negative!")

# Creating object
s1 = Student("Arushi", 90)

# Accessing public attribute
print("Name:", s1.name)

# Accessing private attribute using getter
print("Marks:", s1.get_marks())

# Updating marks using setter
s1.set_marks(95)

# Printing updated marks
print("Updated Marks:", s1.get_marks())
