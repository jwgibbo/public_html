#main.py

from account import Account

def main():
    my_account = Account()
    your_account = Account()

    #my_account._balance = 20
    my_account.deposit(20)

    print(my_account.check_balance())

main()
