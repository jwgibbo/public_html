#main.py

from account import Account

def main():
    
    my_account = Account()

    #deposit 100 dollars in the account
    my_account.deposit(100)

    print(my_account.check_balance())




    #Python added a new member variable
    #on the fly.
    #Lesson: spell your variable right
    #my_account.balance = 5

    #This works. Python won't stop you
    #my_account._balance = 99




main()
