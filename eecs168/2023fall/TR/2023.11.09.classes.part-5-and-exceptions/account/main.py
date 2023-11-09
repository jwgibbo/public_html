#main.py
from account import Account

def main():
    my_account = Account(100)
    your_account = Account(500)


    #    self          other
    if my_account < your_account:
        print('You have more money')
    else:
        print('You do not have more!')

    if my_account > your_account:
        print('I have more money')
    else:
        print('I do not have more money')



main()
