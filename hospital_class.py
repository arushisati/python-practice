# hospital_class.py

class Hospital:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display(self):
        print("Hospital Name :", self.name)
        print("Location      :", self.location)


# Main Program
hospital = Hospital("City Care Hospital", "Delhi")
hospital.display()
