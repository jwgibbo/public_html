#main.py

from account import Account

def main():
    my_account = Account()
    print(my_account.balance)
    my_account.balance = -500000

main()
