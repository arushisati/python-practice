# Private Method Example

class Bank:
    def __show_balance(self):
        print("Balance: ₹50,000")

    def display(self):
        self.__show_balance()

account = Bank()
account.display()
