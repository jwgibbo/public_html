#Goal: Obtain 5 ints from the user

nums = []


for num in range(5):
    user_num = int(input('Enter number: '))
    nums.append(user_num)


print(nums)
print(nums[0])
print('length =', len(nums))
print(type(nums))
print(type(nums[0]))
print(nums[0]*1000)

nums[2] = 99
print(nums)

print('----')

for num in nums:
    print(num)
