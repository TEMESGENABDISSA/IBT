class BankAccount:
    
    def __init__(self, owner, initial_balance=0):

        if initial_balance < 0:
            raise ValueError(
                "Initial balance cannot be negative"
            )

        self.owner = owner
        self._balance = initial_balance


    def deposit(self, amount):

        if amount <= 0:
            raise ValueError(
                "Deposit amount must be positive"
            )

        self._balance += amount


    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError(
                "Withdrawal amount must be positive"
            )

        if amount > self._balance:
            raise ValueError(
                "Insufficient funds"
            )

        self._balance -= amount


    @property
    def balance(self):
        return self._balance


    def __str__(self):

        return (
            f"BankAccount(owner={self.owner}, "
            f"balance={self.balance})"
        )


account = BankAccount("Alice",500)

account.deposit(200)
account.withdraw(100)

print(account)