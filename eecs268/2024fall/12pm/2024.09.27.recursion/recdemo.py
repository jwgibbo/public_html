def rec_func(n):
    if n <= 4:
        print(n)
        rec_func(n+1) #recursive call
    else:
        print('Recursion is over')


def main():
    print('Program starting...')
    rec_func(1) #initial call
    print('Program ending...')

main() 
