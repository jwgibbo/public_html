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
        #is self < other?
        if self._balance < other._balance:
            return True
        else:
            return False
        
    

    def check_balance(self):
        return self._balance

    
