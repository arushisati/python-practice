# payment_polymorphism.py

class Payment:
    def pay(self):
        print("Processing payment")

class CreditCard(Payment):
    def pay(self):
        print("Paid using Credit Card")

class UPI(Payment):
    def pay(self):
        print("Paid using UPI")

class Cash(Payment):
    def pay(self):
        print("Paid using Cash")

payments = [CreditCard(), UPI(), Cash()]

for payment in payments:
    payment.pay()
