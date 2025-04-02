def list_changer(some_list):
    print('some_list =', some_list)
    some_list[0] = 99
    print('some_list =', some_list)

def main():
    nums = [5, 10, 15, 20]
    print('nums =', nums)
    list_changer(nums)
    print('nums =', nums)
    
main()
