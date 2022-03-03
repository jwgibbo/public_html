
def print_stuff():
    print(add_one(99))
    print(add_one(65))
    print(add_one(9))

def add_one(num):
    ans = num + 1
    return ans

def main():
    num = 5
    my_ans = add_one(num)
    print(my_ans)
    print_stuff()

    
main()
