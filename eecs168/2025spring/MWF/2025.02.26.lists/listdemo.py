#Goal: Obtain 5 ints from the user

#Create an empty list
nums = [] 
nums.append(5)
nums.append(10)
nums.append(15)
print(nums)
print(nums[0])
print('---------')
for num in nums:
    print(num)

nums[1] = 55
print(nums)
print(type(nums))
print(type(nums[0]))
print(nums[0] + 2)
