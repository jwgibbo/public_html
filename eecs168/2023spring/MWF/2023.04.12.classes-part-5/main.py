#main.py

from account import Account

def main():
    my_account = Account()
    your_account = Account()

    my_account.deposit(30)
    your_account.deposit(300)

    if my_account < your_account:
        print('I have less money')
    else:
        print('I have more money')

    my_account.deposit(270)
    if my_account == your_account:
        print('Same balances')
    else:
        print('Different balances')
main()
