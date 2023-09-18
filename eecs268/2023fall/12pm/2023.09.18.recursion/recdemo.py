def rec_func(num):
    if num <=4:
        rec_func(num+1) #recursive call
        print(num)
        

def main():
    num = 99
    print('Program starting')
    rec_func(1) #initial call
    print('Program ending')

main()
