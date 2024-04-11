#main.py

from account import Account

def main():
    my_account = Account()
    your_account = Account()
    my_account.deposit(50)
    your_account.deposit(50)
    
    print(my_account.check_balance())

    #  Makes an implicit call to __gt__
    if my_account > your_account:
        print('I have more!')
    else:
        print('Boo! I do not have more')

    if my_account is your_account:
        print('Same object')
    else:
        print('Different objects')

    if my_account == your_account:
        print('Same balance')
    else:
        print('Different balance')
    
 
    

main()
