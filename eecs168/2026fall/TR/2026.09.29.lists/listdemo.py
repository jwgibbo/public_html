# Goal: Store 50 ints

nums = []

for num in range(5):
    user_num = int(input('Enter number: '))
    nums.append(user_num)


print(nums)
print('length =', len(nums))
print(nums[0]*100)
print(nums[2])
# print(nums[99]) ERROR
print(type(nums))
print(type(nums[0]))

print('-----')
for num in nums:
    print(num)
