#account.py

class Account:
    def __init__(self):
        self._balance = 0
        self.test_variable = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            pass

    def withdraw(self, amount):
        #defined Tuesday April 22

    def check_balance(self):
        return self._balance
