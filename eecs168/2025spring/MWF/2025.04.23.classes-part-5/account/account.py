#account.py

class Account:
    def __init__(self):
        self.type = ''
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            pass

    def withdraw(self, amount):
        #we did this as a board work last
        #friday
    
    def check_balance(self):
        return self._balance
