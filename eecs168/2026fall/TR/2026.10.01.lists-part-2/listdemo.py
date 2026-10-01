nums = [11, 22, 33, 44, 55]
print(nums)
nums[0] = 99
print(nums)

# Goal: replace every number with -1
for num in nums:
    num = -1

print(nums)
print('------')

for index in range(len(nums)):
    nums[index] = -1


print(nums)
