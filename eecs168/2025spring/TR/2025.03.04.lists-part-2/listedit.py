nums = [5, 10, 15, 20]

print(nums)
#Put 99 at every index in the list

for num in nums:
    print(num)
    num = 99
    print(num)

print(nums)
print('-----')
for index in range(len(nums)):
    nums[index] = 99

print(nums)
