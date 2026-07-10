# circle_class.py

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def display(self):
        print("Radius :", self.radius)
        print("Area   :", self.area())


# Main Program
circle = Circle(7)
circle.display()
