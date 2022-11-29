#account.py

class Account:
    def __init__(self, staring_balance=0):
        self._balance = 0
        self.deposit(staring_balance)

    def check_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance = self._balance + amount
        else:
            #We need a strong reaction
            #that we'll eventually learn
            #for now, we'll just not change
            #the balance
            pass

    #the self is left argument
    #the other is right argument
    #    self < other
    def __gt__(self, other):
        if self._balance > other._balance:
            return True
        else:
            return False

    def __str__(self):
        output_str = "Account balance: "
        output_str += str(self._balance)
        #Remember to return the str!
        return output_str

    def __repr__(self):
        output_str = f"Account({self._balance})"
        return output_str


