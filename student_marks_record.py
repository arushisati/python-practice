name = input("Enter Student Name: ")
marks = input("Enter Marks: ")

file = open("students.txt", "a")

file.write(name + " - " + marks + "\n")

file.close()

print("Record Saved Successfully")
