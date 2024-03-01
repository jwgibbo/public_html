def num_changer(num):
    print(f'num={num}')
    num = -1
    print(f'num={num}')

def list_changer(nums):
    print(nums)
    nums[0] = -1
    print(nums)
    
def main():
    my_nums = [5, 10, 15]
    print(f'main\'s my_nums = {my_nums}')
    list_changer(my_nums)
    print(f'main\'s my_nums = {my_nums}')
    
    '''    
    num = 5
    print(f'main\'s num = {num}')
    num_changer(num)
    print(f'main\'s num = {num}')
    '''
main()
