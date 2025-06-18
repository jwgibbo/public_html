#Goal: Obtain 5 ints from the user

nums = []

nums.append(5)
nums.append(10)
nums.append(15)

print(nums)
print(nums[2])
print(type(nums))
print(type(nums[2]))


nums[1] = 99
for num in nums:
    print(num)

print('nums has', len(nums), 'elements')
print(nums)
nums.pop(1)
print(nums)
