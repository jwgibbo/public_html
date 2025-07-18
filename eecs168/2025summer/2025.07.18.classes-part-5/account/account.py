#account.py

class Account:
    def __init__(self):
        self._balance = 0

    def transfer_to(self, other, amount):
        

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            #Something went wrong (later lecture)
            pass
        
    def withdraw(self, amount):
        #defined as board work July 17

    def check_balance(self):
        return self._balance
    
