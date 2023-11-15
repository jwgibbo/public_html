#account.py
class Account:
    def __init__(self, first_deposit):
        #This print is for educational use only!
        self._balance = 0 #create a balance
        
        #self._balance = first_deposit
        self.deposit(first_deposit)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            #We'll learn how to react to
            #invalid values
            pass

    def withdraw(self, amount):
        if amount <= self._balance and amount > 0:
            self._balance -= amount
        else:
            #We'll wait on this for now
            pass

    def check_balance(self):
        return self._balance

    def __str__(self):
        output_string = f'balance = '
        output_string += f'{self._balance}'
        return output_string

    def __repr__(self):
        output_string = f'Account({self._balance})'
        return output_string

    def __lt__(self, other):
        print('__lt__called')
        print(f'{self._balance} < {other._balance}')
        if self._balance < other._balance:
            return True
        else:
            return False

    def __eq__(self, other):
        return self._balance == other._balance

    def __ne__(self, other):
        if self == other:
            return False
        else:
            return True
