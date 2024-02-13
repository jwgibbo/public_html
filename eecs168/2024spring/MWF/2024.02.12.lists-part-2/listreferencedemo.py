nums = [5, 10, 15, 20]

for number in nums:
    print(number)

print('=========')
nums[0] = 99
nums[1] = 55

print(nums)

nums2 = nums
print(nums2)

print('=========')

nums2[3] = 88
print(nums)
print(nums2)

print('=========')

temp_num = nums[2]
print(nums)
print(nums2)
print(temp_num)

print('=========')

temp_num = 77
nums[2] = 66
print(temp_num)
print(nums)
print(nums2)

print('=========')

for number in nums:
    number = 0
    print(number)

print(nums)

print('=========')
for index in range(len(nums)):
    print(index)
    nums[index] = 0

print(nums)
print(nums2)
    
