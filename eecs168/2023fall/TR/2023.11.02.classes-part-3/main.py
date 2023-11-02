#main.py
from account import Account

def main():
    my_account = Account(200)
    your_account = Account(100)

    print(my_account.check_balance())
    print(your_account.check_balance())

    #    self          other
    if my_account < your_account:
        print('You have more money')
    else:
        print('You do not have more!')
    

main()
