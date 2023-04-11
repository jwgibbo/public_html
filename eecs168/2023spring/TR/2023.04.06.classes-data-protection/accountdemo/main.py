#main.py

from account import Account

def main():
    my_account = Account()
    my_account.deposit(100) #works
    my_account.deposit(-100) #fails
