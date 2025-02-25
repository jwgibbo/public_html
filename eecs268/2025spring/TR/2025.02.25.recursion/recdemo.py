def rec_func(num):
    if num <= 3:
        print(num)
        rec_func(num+1) #recursive call
    else:
        print('num =', num, ' recursion done')

def main():
    num = 99
    print('Program started...')
    rec_func(1) #initial call
    print('Program ending...')

main()
