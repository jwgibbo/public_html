#Goal: Obtain 50 ints from the user

nums = [5, 10, 15, 20, 25]

print(nums)
print(nums[2])

print(type(nums))
print(type(nums[2]))
print('-----')
nums[0] = 99
nums.append(55)
for num in nums:
    print(num)

print('nums has', len(nums), 'elements')
