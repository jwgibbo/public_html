#main.py

from account import Account

def main():
    my_account = Account()
    my_account.deposit(100) #works


    your_account = Account()
    your_account.deposit(5000)

    if my_account < your_account:
        print('I have fewer space bucks')
    else:
        print('I have more space bucks')


main()
