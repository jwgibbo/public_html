#account.py

class Account:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            #amount is invalid
            #we'll learn an appropriate
            #reaction. For now, we'll
            #do nothing
            pass

    def withdraw(self, amount):
        #your definition here
        pass

    def __lt__(self, other):
        return self._balance < other._balance

    def __str__(self):
        return f'Account: balance=${self._balance}' 

    def __repr__(self):
        return f'Account({self._balance})'

