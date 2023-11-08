#main.py
from account import Account

def main():
    my_account = Account(100)
    your_account = Account(100)
    bank = [my_account, your_account]
    print(my_account)
    print(your_account)
    print(bank)

    evil_bank = [Account(100), Account(100)]
    print(evil_bank)

    #    self          other
    if my_account < your_account:
        print('You have more money')
    else:
        print('You do not have more!')

    if my_account == your_account:
        print('Accounts are the same')
    else:
        print('Accounts are different')    

    if my_account != your_account:
        print('Accounts are different')
    else:
        print('Accounts are the same')

main()
