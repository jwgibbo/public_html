class Account:

    def __init__(self):

        #convention to indicate
        #the member should NOT be
        #directly interacted with
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount < self._balance and amount > 0:
            self._balance -= amount

    def check_balance(self):
        return self._balance
