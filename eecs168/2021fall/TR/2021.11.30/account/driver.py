from account import Account

def main():
    my_account = Account()

    my_account.deposit(100)

    #still possible, but don't do it!
    my_account._balance = 10000000

    print(my_account.check_balance())

if __name__ == '__main__':
    main()
