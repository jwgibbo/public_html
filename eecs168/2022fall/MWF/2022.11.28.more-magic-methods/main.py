#main.py

from account import Account

def main():
    
    my_account = Account() #calls __init__
    your_account = Account() #call __init__

    #deposit 100 dollars in the account
    my_account.deposit(100)

    your_account.deposit(100)


    if your_account == my_account:
        print('Same balance')
    else:
        print('Different balance')



main()
