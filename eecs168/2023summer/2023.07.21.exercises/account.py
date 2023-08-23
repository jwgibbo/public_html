#account.py


class Account:
    def __init__(self):
        self._balance = 0
        self.temp = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            #we'll learn a strong reaction
            #for now, we'll just pass
            pass
        
    def withdraw(self, amount):
        #define
        
