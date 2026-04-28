#account.py

class Account:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance = self._balance + amount
        else:
            pass #TODO finish this else

    def check_balance(self):
        return self._balance
