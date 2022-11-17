#main.py

from account import Account

def main():

    #makes new variables
    x = 5
    z = 10
    
    my_account = Account()#call __init__
    your_account = Account()
    
    my_account.deposit(100)
    your_account.deposit(2)

    if your_account > my_account:
        print("Wait, I thought I stole all your money!")
    else:
        print("Frank stole your money")
    


    #Works but voiolates convention
    #my_account._balance = -50
    #print(my_account._balance)
    
    #Works, but should never be done
    #my_account.balance = -50

    

main()
