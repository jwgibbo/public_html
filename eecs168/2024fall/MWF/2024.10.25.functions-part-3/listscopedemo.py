def main():
    nums = [5, 10, 15]
    print("main's nums", nums)
    list_changer(nums)
    print("main's nums", nums)

def list_changer(some_list):
    print("list_changer's list", some_list)
    some_list[0] = -1
    print("list_changer's list", some_list)
    print('Ha ha ha!')

main()
