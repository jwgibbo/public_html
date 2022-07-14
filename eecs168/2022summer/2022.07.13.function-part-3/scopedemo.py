def num_changer(x):
    print(f'x={x}')
    x = 99
    print(f'x={x}')    

def element_changer(nums):
    print(nums)
    nums[0] = 99
    print(nums)
    

def main():
    x = 5
    print(f'x={x}')
    num_changer(x)
    print(f'x={x}')

    nums = [5, 10, 15, 20]
    print(nums)
    element_changer(nums)
    print(nums)

#Only "global" function call
main()
