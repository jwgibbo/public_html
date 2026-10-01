nums = []

for num in range(10, 15):
    nums.append(num)


print(nums)
nums[0] = 99
print(nums)

for num in nums:
    num = -1
print(nums)
print('--------')
for index in range(len(nums)):
    nums[index] = -1

print(nums)
