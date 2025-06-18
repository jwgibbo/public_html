def rec_func(num):
    if num <= 5:
        rec_func(num+1) #recursive call
        print(num)
    else:
        print('Done recursing. num =', num)

def main():
    rec_func(1) #initial call to rec_func

main()
