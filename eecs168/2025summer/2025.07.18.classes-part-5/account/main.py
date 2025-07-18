#main.py

from account import Account

def main():
    my_account = Account()
    your_account = Account()

    #my_account._balance = 20
    my_account.deposit(20)
    your_account.deposit(500)

    print(my_account.check_balance())

    your_account.transfer_to(my_account, 50)

    print(my_account.check_balance()) #70
    print(your_account.check_balance()) #450
    

main()
