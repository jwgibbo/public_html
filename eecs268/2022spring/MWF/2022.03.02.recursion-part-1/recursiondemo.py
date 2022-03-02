def add_one(num):
    ans = num + 1
    return ans

def rec_func(i):
    if i < 3:
        print('Hello')
        rec_func(i+1) #recursive call
        


def main():
    rec_func(0) #initial call
    print('Goodbye')

main()
