#main.py

from account import Account

def main():
    my_account = Account()
    your_account = Account()
    my_account.deposit(50)
    your_account.deposit(50)
    print(my_account.check_balance())

    if my_account > your_account:
        print('haha I have more!')


main()
