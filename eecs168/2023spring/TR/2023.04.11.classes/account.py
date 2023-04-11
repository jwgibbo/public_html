#account.py

class Account:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            pass
            #We'll learn a better
            #reaction

    def __lt__(self, other):
        return self._balance < other._balance

        
