nums = [5, 10, 15, 20]
print(nums)
print(len(nums))
print('--------')
for num in nums:
    print(num)
print('-----')
print(nums)
print('------')
#Goal: change all the values to -1
for num in nums:
    print(num, end=' ')
    num = -1
    print(num)

print(nums)

#Now let's try looping over the indexes
for index in range(len(nums)):
    nums[index] = -1

print(nums)
