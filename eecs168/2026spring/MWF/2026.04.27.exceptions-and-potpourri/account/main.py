#main.py

from account import Account

def main():
    my_account = Account()

    my_account.deposit(10)
    my_account.deposit(-20)#needs a try-except
    
    print('current balance:')
    print(my_account.check_balance())

main()
