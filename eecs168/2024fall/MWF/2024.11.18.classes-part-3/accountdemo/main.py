#main.py

from account import Account

def main():
    my_account = Account()

    #my_account.balance = -1000

    my_account.deposit(50)
    print(my_account.check_balance())
    my_account.deposit(-1000)
    print(my_account.check_balance())

main()
