#main.py

from account import Account

def main():
    my_account = Account(1)
    your_account = Account(2)
    their_account = Account(1)
    
    my_account.deposit(50)
    your_account.deposit(50)
    print(my_account)
    print(your_account)

    bank = []
    bank.append(my_account)
    bank.append(your_account)
    print(bank)
    
    if my_account > your_account:
        print('haha I have more!')
    else:
        print('oh no, I do not have more')


    if my_account is your_account:
        print('Same')
    else:
        print('Different')


main()
