#account.py

class Account:
    def __init__(self, start_balance):
        self._balance = 0
        self.deposit(start_balance)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            #redefine to raise ValueError

    def check_balance(self):
        return self._balance
            

    
