#account.py

class Account:
    def __init__(self):
        self.type = ''
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('amount invalid for deposit') 

    def check_balance(self):
        return self._balance
