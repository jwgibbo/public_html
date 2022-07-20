
def num_changer(num):
    print(f'num={num}')
    num = 99
    print(f'num={num}')

def element_changer(nums):
    print(f'nums={nums}')
    nums[0] = 99
    print(f'nums={nums}')

def main():
    #First visualization in notes
    x = 5
    print(f'x={x}')
    num_changer(x)
    print(f'x={x}')

    #Second visualization in notes
    my_nums = [5, 10, 15, 20]
    print(f'my_nums={my_nums}')
    element_changer(my_nums)
    print(f'my_nums={my_nums}')

main()
