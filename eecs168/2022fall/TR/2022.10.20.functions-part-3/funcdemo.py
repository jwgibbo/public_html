def elem_changer(some_list):
    some_list[0] = 2

def main():
    nums = [5, 10, 15, 20]
    print(nums)
    elem_changer(nums)
    print(nums)

main()
