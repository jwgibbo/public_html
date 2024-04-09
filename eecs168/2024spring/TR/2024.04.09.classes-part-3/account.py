#account.py

class Account:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            pass

    def withdraw(self, amount):
        #define this
        pass

    def transfer(self, other, amount):
        #define this
        pass

    def check_balance(self):
        return self._balance

    def __gt__(self, other):
        if self._balance > other._balance:
            return True
        else:
            return False
