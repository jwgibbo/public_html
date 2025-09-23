def rec_func(num):
    if num <= 5:
        rec_func(num+1) #recursive call
        print(num)
    else:
        print('Recursion ending. num =', num)


def main():
    print('Program started')
    rec_func(1) #initial call
    print('Program ending...')

main()
