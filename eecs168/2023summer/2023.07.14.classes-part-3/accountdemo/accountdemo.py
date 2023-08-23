#accountdemo

from account import Account


def main():
    my_account = Account()
    your_account = Account()

    my_account.deposit(50)
    your_account.deposit(51)


main()
