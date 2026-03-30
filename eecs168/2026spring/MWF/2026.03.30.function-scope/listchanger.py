def list_changer(nums):
    print(nums)
    nums[0] = -1 #Muhahahaha!
    print(nums)

def main():
    nums = [5, 10, 15, 20]
    list_changer(nums)
    print("main's list after call:", nums)

main()
