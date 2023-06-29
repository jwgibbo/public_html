nums = [5, 10, 15]

print(nums)
for num in nums:
    print('num =', num)
    num = 0
    print('num =', num)

print(nums)


for index in range(0, len(nums)):
    nums[index] = 0


print(nums)
