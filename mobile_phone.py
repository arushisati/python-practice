class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)


m1 = Mobile("Samsung", "S25", 85000)
m2 = Mobile("Apple", "iPhone 17", 120000)

m1.display()
print()
m2.display()
