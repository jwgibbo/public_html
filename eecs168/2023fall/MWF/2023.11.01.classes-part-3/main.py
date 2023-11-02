#main.py
from account import Account

def main():
    my_account = Account(0)
    my_account.deposit(50)
    my_account.deposit(25)
    print(my_account.check_balance())

    your_account = Account(2000)
    your_account.deposit(100)
    your_account.deposit(75)
    print(your_account.check_balance())
    
    if my_account < your_account:
        print('You have more money')
    else:
        print('I have more money')

    
main()
