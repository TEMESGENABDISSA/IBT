# Parent class
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    # Add money
    def deposit(self, amount):
        self.balance += amount

    # Show account info
    def show(self):
        print(f"{self.name} : {self.balance} ETB")


# Child class
class SavingAccount(Account):
    # Override parent method
    def show(self):
        print(f"Saving Account -> {self.name} : {self.balance} ETB")


# Child class
class CurrentAccount(Account):
    # Override parent method
    def show(self):
        print(f"Current Account -> {self.name} : {self.balance} ETB")


# Child class
class BusinessAccount(Account):
    # Override parent method
    def show(self):
        print(f"Business Account -> {self.name} : {self.balance} ETB")


# Create one object
acc = SavingAccount("Temesgen", 5000)

# Two variables point to the same object
a = acc
b = acc

# Change balance using 'a'*
a.deposit(2000)

# Both show the updated balance
a.show()
b.show()