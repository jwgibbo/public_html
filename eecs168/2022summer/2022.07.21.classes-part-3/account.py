#account.py

class Account:
    def __init__(self):
        self._balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount

    def check_balance(self):
        return self._balance
