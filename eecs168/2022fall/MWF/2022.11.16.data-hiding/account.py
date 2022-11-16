#account.py


class Account:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            #We don't know how to
            #have a good response
            pass

    def check_balance(self):
        return self._balance
