#mapdemo.py

list_of_strings = ['5', '10', '15']
print(list_of_strings)

#long way of converting every value to ints
for index in range(len(list_of_strings)):
    list_of_strings[index] = int(list_of_strings[index])

print(list_of_strings)

#shorter way, using map
list_of_strings = ['5', '10', '15']
print(list_of_strings)
nums = list(map(int, list_of_strings))
print(nums)
print(list_of_strings)
