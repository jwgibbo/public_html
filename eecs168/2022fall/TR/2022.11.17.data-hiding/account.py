#account.py

class Account:
    def __init__(self):
        self._balance = 0

    def check_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance = self._balance + amount
        else:
            #We need a strong reaction
            #that we'll eventually learn
            #for now, we'll just not change
            #the balance
            pass

    #the self is left argument
    #the other is right argument
    #    self < other
    def __gt__(self, other):
        if self._balance > other._balance:
            return True
        else:
            return False


