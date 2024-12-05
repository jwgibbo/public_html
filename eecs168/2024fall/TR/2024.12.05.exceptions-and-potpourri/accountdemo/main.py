#main.py
from account import Account
def main():
    my_account = Account(2)
    my_account.deposit(8.50)
    print(my_account.check_balance())
    my_account.deposit(-1000)
    print(my_account.check_balance())

    your_account = Account(1_000_000)
    if your_account.is_larger(my_account):
        print('you have more money')
    else:
        print('I have more money')

main()
