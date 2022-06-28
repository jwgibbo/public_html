nums = [5, 10, 15, 20]

print(nums)

print('======')

for num in nums:
    print(num)
    num = 99
    print(num)

print('======')

print(nums)

print('======')


first_element = nums[0]
print(first_element)
first_element = 99
print(first_element)
print(nums[0])

print('======')

nums2 = nums #They refer to same list
nums[0] = 99
print(nums)
print(nums2)

print('======')
nums2.append(28)
print(nums)
print(nums2)

print('======')

letters = ['a', 'b', 'c']
letters2 = ['a', 'b', 'c']
print(letters == letters2)
print(letters < letters2)
letters[0] = 'z'
print(letters)
print(letters2)


