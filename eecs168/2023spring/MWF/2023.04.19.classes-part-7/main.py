#main.py

from account import Account

def main():
    my_account = Account(30)
    your_account = Account(300)

    #my_account.deposit(30)
    #your_account.deposit(300)

    print(my_account)
    print(your_account)

    bank = [] #empty list
    bank.append(my_account)
    bank.append(your_account)
    print(bank)
    
main()
