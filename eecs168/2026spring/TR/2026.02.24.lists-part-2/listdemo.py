nums = [5, 10, 15, 20]

for num in nums:
    print(num)

print('------')

#Goal: Change all values in the list to -1
for num in nums:
    print(num)
    num = -1
    print(num)

print(nums)
print('--------')

for index in range(len(nums)):
    print('index =', index, 'nums[index] =', nums[index])
    nums[index] = -1

print(nums)
    
