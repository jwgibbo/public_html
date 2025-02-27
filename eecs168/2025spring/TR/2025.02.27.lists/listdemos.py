#Goal: Obtain 5 ints from the user
nums = []
nums.append(5)
nums.append(10)
nums.append(15)
print(nums)
print('length =', len(nums))
print(nums[0])
print('-----')
nums[0] = 99
for num in nums:
    print(num)

print('-------')
print(type(nums))
print(type(nums[0]))
print(nums[1]+2)

