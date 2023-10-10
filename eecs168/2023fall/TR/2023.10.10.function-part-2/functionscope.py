def num_changer(num):
    print("num_changer's num=", num)
    num = -1 #Hahaha
    print("num_changer's num=", num)
    return 

def list_changer_v1(some_list):
    print('some_list =', some_list)
    some_list[0] = -1 #Hahaha
    print('some_list =', some_list)

def list_changer_v2(some_list):
    print('some_list =', some_list)
    some_list = -1 #Hahaha
    print('some_list =', some_list)

def main():
    value = 5
    print("main's value =", value)
    num_changer(value)
    print("main's value =", value)

    nums = [5, 10, 15, 20]
    print('nums =', nums)
    list_changer_v1(nums)
    print('nums =', nums)

    nums = [5, 10, 15, 20]
    print('nums =', nums)
    list_changer_v2(nums)
    print('nums =', nums)


main()
