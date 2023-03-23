def num_change(num):
    print('Your num was', num)
    num = 5
    print('But now it is:', num)

def list_change(some_list):
    some_list[0] = 99

def main():
    #first visualization
    value = 10
    num_change(value)

    print("Now we're back in main")
    print('value is', value)

    #second visualization
    nums = [5, 10, 15, 20]
    print(nums)
    list_change(nums)
    print(nums)

main()
