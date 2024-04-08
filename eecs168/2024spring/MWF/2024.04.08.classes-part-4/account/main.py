#main.py

from account import Account

def main():
    my_account = Account()
    your_account = Account()
    my_account.deposit(50)
    my_account.transfer(your_account, 10)
    print(my_account.check_balance())
 
    

main()
