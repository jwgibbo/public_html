fruits = 'apple,orange,kiwi'
fruits_list = fruits.split(',')
print(fruits_list)

delimiter = '\t'
dashed_fruits = delimiter.join(fruits_list)
print(dashed_fruits)
