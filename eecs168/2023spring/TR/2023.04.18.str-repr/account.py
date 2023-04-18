#account.py

class Account:
    def __init__(self, owner, account_id):
        self._balance = 0
        self._owner = owner
        self._account_id = account_id

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            pass
            #We'll learn a better
            #reaction

    def __lt__(self, other):
        return self._balance < other._balance

    def __eq__(self, other):
        is_same_balance = (self._balance == other._balance)
        is_same_owner = (self._owner == other._owner)
        is_same_id = (self._account_id == other._account_id)
        return is_same_balance and is_same_owner and is_same_id

    def __ne__(self, other):
        return not(self == other)

    def __str__(self):
        output_string = f'Account: owner={self._owner}'
        output_string += f' id={self._account_id}'
        output_string += f' balance={self._balance}'
        return output_string

    def __repr__(self):
        return f'Account("{self._owner}", {self._account_id})'
    
