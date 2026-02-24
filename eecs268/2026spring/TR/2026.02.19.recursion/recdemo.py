def rec_func(num):
    if num <= 4:
        print(num)
        rec_func(num+1) #recursive call
        
    else:
        print(num, 'Recursion over...')

def main():
    print('Program starting...')
    rec_func(1) #initial call
    print('Program ending...')

main()
