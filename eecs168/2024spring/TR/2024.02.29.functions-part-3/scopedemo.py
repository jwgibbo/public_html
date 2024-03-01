def num_changer(num):
    print(f'num={num}')
    num = -1
    print(f'num={num}')
    #FREEEZE code look at diagram 1

def list_changer(nums):
    print(nums)
    nums[0] = -1
    print(nums)
    #FREEZE code look at diagram 2

def main():
    number_jack = 5
    print(f'number_jack={number_jack}')
    num_changer(number_jack)
    print(f'number_jack={number_jack}')


    my_numbers = [5, 10, 15, 20]
    print(f'my_numbers={my_numbers}')
    list_changer(my_numbers)
    print(f'my_numbers={my_numbers}')

main()
