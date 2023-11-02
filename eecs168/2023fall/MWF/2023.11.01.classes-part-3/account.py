#account.py
class Account:
    def __init__(self, first_deposit):
        #This print is for educational use only!
        print('Account\'s init called')

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
