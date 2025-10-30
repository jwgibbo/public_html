def list_changer(some_list):
    print("list_changer's list", some_list)
    some_list[0] = -1
    some_list.append(99)
    print("list_changer's list", some_list)

def main():
    nums = [5, 10, 15, 23]
    print("main's nums", nums)
    list_changer(nums)
    print("main's nums", nums)

main()
