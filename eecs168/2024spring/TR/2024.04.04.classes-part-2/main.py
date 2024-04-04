#main.py

from account import Account

def main():
    my_account = Account()
    my_account.deposit(50)
    print(my_account._balance)


main()
