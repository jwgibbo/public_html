def rec_func(num):
    if num <= 5:
        print(num)
        rec_func(num+1) #recursive call
    else:
        print('recursion over')
        

def main():
    print('Program started...')
    rec_func(1) #initial call
    print('Program ended...')

main()
