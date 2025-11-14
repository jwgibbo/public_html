#main.py

from account import Account

def main():
    my_account = Account()

    my_account.deposit(5)
    my_account.deposit(-100)

    print('my balance is', my_account.check_balance())    

main()
