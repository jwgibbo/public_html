#main.py

from account import Account

def main():
    
    my_account = Account() #calls __init__
    your_account = Account() #call __init__

    #deposit 100 dollars in the account
    my_account.deposit(100)

    your_account.deposit(1000)


    if your_account > my_account:
        print('Yay, my students aren\'t richer than me!')
    else:
        print('Shucks. I knew teaching wasn\'t going to pay off')



main()
