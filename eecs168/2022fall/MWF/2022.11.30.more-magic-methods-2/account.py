#account.py


class Account:
    def __init__(self, start_balance=0):
        self._balance = 0
        self.deposit(start_balance)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            #We don't know how to
            #have a good response
            pass

    def check_balance(self):
        return self._balance

    def __lt__(self, other):
        if self._balance < other._balance:
            return True
        else:
            return False

    def __eq__(self, other):
        if self._balance == other._balance:
            return True
        else:
            return False

    def __str__(self):
        output_str = f'Account with balance: ${self._balance}'
        return output_str

    def __repr__(self):
        output_str = f'Account({self._balance})'
        return output_str
