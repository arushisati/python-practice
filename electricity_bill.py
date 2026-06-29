class ElectricityBill:
    def __init__(self, units):
        self.units = units

    def calculate(self):
        return self.units * 8


bill = ElectricityBill(120)

print("Electricity Bill:", bill.calculate())
