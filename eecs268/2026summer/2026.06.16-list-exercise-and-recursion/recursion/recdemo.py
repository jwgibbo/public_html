#recdemo.py

def rec_func(num):
    if num <= 4:
        rec_func(num+1) #recursive call
        print(num)
    else:
        print('recursion ended')
        

def main():
    print('Program started')
    rec_func(1) #initial call
    print('Program ending...')

main()
