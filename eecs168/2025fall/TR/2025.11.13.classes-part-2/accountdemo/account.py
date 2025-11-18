#account.py

class Account:
    def __init__(self):
        self._balance = 0
        self.dummy = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance = self._balance + amount


    def withdraw(self, amount):
        #defined Nov 18

    def check_balance(self):
        return self._balance
