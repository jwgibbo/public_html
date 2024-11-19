#account.py

class Account:
    def __init__(self, start_balance):
        self._balance = 0
        self.deposit(start_balance)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            #we'll learn this later
            pass

    def check_balance(self):
        return self._balance
            

    
