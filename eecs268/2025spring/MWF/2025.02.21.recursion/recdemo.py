def rec_func(num):
    if num <= 10:
        print(num)
        rec_func(num+1)  
    else:
        print('recursion ending...')

def main():
    print('program starting...')
    num = 99
    rec_func(1)
    print('program ending...')

main()
