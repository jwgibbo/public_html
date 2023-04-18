#main.py

from account import Account

def main():
    my_account = Account('john', 123)
    my_account.deposit(100) #works


    your_account = Account('students', 345)
    your_account.deposit(5000)

    print(my_account)
    print(your_account)

    bank = [] #list of Accounts
    bank.append(my_account)
    bank.append(your_account)

    print(bank)

    other_bank = [Account('john', 123), Account('students', 345)]
    print(other_bank)


main()
