#main.py

from account import Account

def main():
    
    my_account = Account() #calls __init__
    your_account = Account() #call __init__

    #deposit 100 dollars in the account
    my_account.deposit(100)

    your_account.deposit(10)

    their_account = Account()

    #Each print makes an implicit
    #call to Account's __str__
    print(my_account)
    print(your_account)

    bank = [my_account, your_account]
    print(bank)



main()
