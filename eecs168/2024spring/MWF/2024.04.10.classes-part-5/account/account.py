#account.py

class Account:
    def __init__(self):
        self._balance = 0

    def withdraw(self, amount):
        #define here
        pass

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            #we'll learn how to react later
            pass

    def check_balance(self):
        return self._balance
        
    def __gt__(self, other):
        if self._balance > other._balance:
            return True
        else:
            return False

    def __eq__(self, other):
        if self._balance == other._balance:
            return True
        else:
            return False