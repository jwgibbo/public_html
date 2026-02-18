def rec_func(num):
    if num <= 4:
        print(num)
        num = num+1
        rec_func(num) #recursive call
    else:
        print('num =', num, 'Recursion over!')
def main():
    print('Program started...')

    rec_func(1) #initial call

    print('Program ending...')
    
main()
