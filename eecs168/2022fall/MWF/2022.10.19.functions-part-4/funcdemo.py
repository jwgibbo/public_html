def evil_func(num):
    print(num)
    num = -1
    print(num)
    print("Muahaha")

def element_changer(some_list):
    some_list[0] = "Boo!"

def cool_printer(some_list):
    for elem in some_list:
        print(elem, 'wow!')
    
def main():
    '''
    num = 5
    print(num)
    evil_func(num)
    print(num)
    '''
    
    nums = [5, 10, 15, 20]
    nums[2] = 99
    print(nums)
    element_changer(nums)
    print(nums)
    cool_printer(nums)

main()
