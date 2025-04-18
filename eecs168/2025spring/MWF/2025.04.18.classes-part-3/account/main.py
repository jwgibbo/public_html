#main.py

from account import Account

def main():
    my_account = Account()
    my_account.type = 'savings'
    my_account.deposit(20)

    print(my_account.check_balance())

main()
