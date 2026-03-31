def list_changer(nums):
    print('list changer nums=', nums)
    nums[0] = -1
    print('list changer nums=', nums)

def main():
    nums = [5, 10, 15, 20]
    print('main nums =', nums)
    list_changer(nums)
    print('main nums =', nums)

main()
