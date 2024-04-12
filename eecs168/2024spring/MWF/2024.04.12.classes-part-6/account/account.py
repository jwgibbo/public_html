#account.py

class Account:
    def __init__(self, start_balance):
        self._balance = 0
        self.deposit(start_balance)

    def __str__(self):
        output_str = 'Account with $'
        output_str += str(self._balance)
        return output_str

    def __repr__(self):
        output_str = f'Account({self._balance})'
        return output_str

    def withdraw(self, amount):
        #define here
        pass

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            #we'll learn how to react later
            pass

    def check_balance(self):
        return self._balance
        
    def __gt__(self, other):
        if self._balance > other._balance:
            return True
        else:
            return False

    def __eq__(self, other):
        if self._balance == other._balance:
            return True
        else:
            return False
