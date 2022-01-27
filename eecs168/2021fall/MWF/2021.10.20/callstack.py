

def num_changer(num):
    print("num = ", num)
    num = -99
    print("num = ", num)

def list_changer(the_list):
    print("the_list = ", the_list)
    the_list[0] = -99
    print("the_list = ", the_list)

def main():
    x = 5
    print("x = ", x)
    num_changer(x)
    print("x = ", x)

    nums = [5, 10, 15]
    print("nums = ", nums)
    list_changer(nums)
    print("nums = ", nums)

main()
