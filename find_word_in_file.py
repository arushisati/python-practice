file = open("sample.txt", "r")

data = file.read()

if "Python" in data:
    print("Word Found")
else:
    print("Word Not Found")

file.close()
