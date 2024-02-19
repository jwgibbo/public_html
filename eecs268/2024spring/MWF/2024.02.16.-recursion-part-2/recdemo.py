def rec_func(num):
    if num <= 5:
        print(num)
        rec_func(num+1) #recursive call
        

def main():
    rec_func(1) #initial call
    print('Program ending')

main()
