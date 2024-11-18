#account.py

class Account:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            #we'll learn what to do later
            pass

    def check_balance(self):
        return self._balance
