#main.py

from account import Account

def main():
    my_account = Account('john', 123)

    my_account.deposit(-100) #works
    print(my_account.check_balance())




main()
