#main.py

from account import Account

def main():
    my_account = Account()
    my_account.type = 'savings'
    my_account.deposit(20)

    your_account = Account()
    your_account.deposit(100)

    if my_account == your_account:
        print('they are same')
    else:
        print('they are different')

    print(my_account.check_balance())

main()
