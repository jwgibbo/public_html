#main.py
from account import Account

def main():
    my_account = Account(50)
    your_account = Account(100)
    #    self          other
    if my_account < your_account:
        print('You have more')
    else:
        print("You don't have more")
main()
