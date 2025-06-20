nums = [5, 10, 15, 20]

test = nums[0]
print(test, nums[0])
test = 99
print(test, nums[0])


#Goal: Change all the numbers to 0
for num in nums:
    print(num, end=' ')
    num = 0
    print(num)

print(nums)

for index in range(0, len(nums)):
    nums[index] = 0

print(nums)
