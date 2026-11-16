#main.py

from account import Account

def main():
    my_account = Account()
    my_account.deposit(10)

    print(my_account.check_balance())
main()
