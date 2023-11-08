#account.py
class Account:
    def __init__(self, first_deposit):
        #this print is for
        #educational purposes only!
        print("Account's init called")
        self._balance = 0 #creates balance
        self.deposit(first_deposit)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            #We'll learn an appropriate
            #reaction to bad amounts
            pass

    def __lt__(self, other):
        print('__lt__ called')
        #is self < other?
        if self._balance < other._balance:
            return True
        else:
            return False

    def __eq__(self, other):
        print('__eq__ called')
        return self._balance == other._balance

    def __ne__(self, other):
        print('__ne__ called')
        if self == other:
            return False
        else:
            return True

    def __str__(self):
        output = "U hav dis amnt of $$$: "
        output = output + str(self._balance)
        return output

    def __repr__(self):
        output = "Account(" + str(self._balance) + ")"
        return output
        
    def check_balance(self):
        return self._balance

    
