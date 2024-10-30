#listscopedemo.py

def list_changer(some_list):
    print(f"list_changer's list =", some_list)
    some_list[0] = -1
    print(f"list_changer's list =", some_list)

def main():
    nums = [5, 10, 15]
    nums2 = [99, 100, 101]
    print(f"main's list =", nums)
    list_changer(nums)
    print(f"main's list =", nums)

main()
