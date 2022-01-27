nums = [5, 10, 15, 20]
temp = nums[-1]
nums[-1] = nums[0]
nums[0] = temp

for num in nums:
    num = num + 1
    print(num)


print("Original list:")
print(nums)

for index in range(0,len(nums)):
    nums[index] = nums[index] + 1

print("Original list:")
print(nums)
