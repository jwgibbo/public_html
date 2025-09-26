#Goal: Change all numbers to -1

nums = [5, 10, 15, 20]

print(nums)

for num in nums:
    print(num)
    num = -1
    print(num)

print(nums)

for index in range(len(nums)):
    nums[index] = -1

print(nums)
    
