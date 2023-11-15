#main.py

from account import Account

def main():
    my_account = Account(50)
    your_account = Account(2)

    my_account.deposit(100)
    your_account.deposit(5000)

    print(my_account)
    print(your_account)

    bank = []
    bank.append(my_account)
    bank.append(your_account)

    print(bank)

main()
