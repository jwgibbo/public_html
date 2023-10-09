def num_changer(num):
    print('num_changer\'s num =', num)
    num = -1 #Hahaha!
    print('num_changer\'s num =', num)
    return

def list_appender(some_list):
    some_list.append(99)

def list_changer_v1(some_list):
    print('some_list =', some_list)
    some_list[0] = -1 #hahaha!
    print('some_list =', some_list)
    return

def list_changer_v2(some_list):
    print('some_list =', some_list)
    some_list = -1 #hahaha!
    print('some_list =', some_list)
    return

def main():
    num = 5
    print('main\'s num =', num)
    num_changer(num)
    print('main\'s num = ', num)

    print('=======')

    nums = [5, 10, 15, 20]
    print('nums[0] =', nums[0])
    list_changer_v1(nums)
    print('nums[0] =', nums[0])

    print('=======')

    print('nums[0] =', nums[0])
    list_changer_v2(nums)
    print('nums[0] =', nums[0])

    print('=======')

    print(nums)
    list_appender(nums)
    print(nums)
    
main()
