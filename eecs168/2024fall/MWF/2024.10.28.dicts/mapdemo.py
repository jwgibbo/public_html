strings = ['2.5', '7.7', '10.2']
'''
print(strings)
for index in range(len(strings)):
    strings[index] = float(strings[index])
print(strings)
'''
nums = list(map(float, strings))
print(strings)
print(nums)
