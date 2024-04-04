#account.py

class Account:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount
