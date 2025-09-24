nums = [5, 10, 15, 20]

print(nums)

#Goal: Change all the numbers to -1
for num in nums:
    print(num)
    num = -1
    print(num)

print(nums)

for index in range(0, len(nums)):
    nums[index] = -1


print(nums)
