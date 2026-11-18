#main.py

from account import Account

def main():
    my_account = Account(10) #init called

    print(my_account.check_balance())
main()
