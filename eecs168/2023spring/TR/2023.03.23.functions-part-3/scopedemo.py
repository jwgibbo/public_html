def funkytown():
    x = 5
    print(x)

def num_change(num):
    print('num was', num)
    num = 13
    print('but now it is', num)

def list_change(some_list):
    some_list[0] = 99

def main():
    #First visualization
    value = 5
    num_change(value)

    print('Now we are back in main')
    print('value is', value)

    #Second visualization
    nums = [5, 10, 15, 20]
    print(nums)
    list_change(nums)
    print(nums)

main()


