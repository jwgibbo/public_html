#Goal store 5 ints from the user

nums = []
print(nums)
print(type(nums))

nums.append(5)
nums.append(10)
nums.append(15)
nums.append(20)
print(nums)
print(nums[2])
nums[0] = 99
print('---------')
for num in nums:
    print(num)


words = ['cat', 'doggy', 'pizza', 'fish']
for word in words:
    print(word[0])

print(words[0][0])
