def add_one(num):
    ans = num + 1
    return ans

def rec_func(i):
    if i < 3:
        print(i)
        rec_func(i+1) #recursive call
        
        
        


def main():
    rec_func(0)

    print('=========')
    i = 0
    while i<3:
        i = i + 1
        print(i)

main()
