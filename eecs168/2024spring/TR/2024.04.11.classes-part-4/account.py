#account.py

class Account:
    def __init__(self, start_balance):
        self._balance = start_balance
        
    def __repr__(self):
        output_str = f'Account({self._balance})'
        return output_str
    
    def __str__(self):
        output_str = 'Account with balance: '
        output_str += str(self._balance)
        return output_str
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            pass

    def withdraw(self, amount):
        #define this
        pass

    def transfer(self, other, amount):
        #define this
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







    
