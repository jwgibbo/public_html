#account.py

class Account:
    def __init__(self, starting_balance):
        print('init called')
        self._balance = 0
        self.deposit(starting_balance)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def check_balance(self):
        return self._balance

    #add withdraw method here (wednesday)

    #add a transfer method here (Friday)
