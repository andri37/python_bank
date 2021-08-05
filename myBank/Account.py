class Account:
    def __init__(self):
        self.account_balance = 0

    def withdraw(self, amount: float):
        if amount > self.account_balance:
            print(f"Your balance is {self.account_balance} €")
        else:
            self.account_balance -= amount
            print(f"You withdrew {amount} €. Your balance is now {self.account_balance} €")

