#main.py

from account import Account

def main():
    my_account = Account(10)
    your_account = Account(5)
    my_account.deposit(50)
    your_account.deposit(50)
    bank = []
    bank.append(my_account)
    bank.append(your_account)
    
    print(my_account) #uses __str__
    print(your_account) #uses __str__
    print(bank) #uses __repr__
    

main()
