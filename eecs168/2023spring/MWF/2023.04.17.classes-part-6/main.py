#main.py

from account import Account

def main():
    my_account = Account()
    your_account = Account()

    my_account.deposit(30)
    your_account.deposit(300)

    print(my_account)
    print(your_account)
main()
