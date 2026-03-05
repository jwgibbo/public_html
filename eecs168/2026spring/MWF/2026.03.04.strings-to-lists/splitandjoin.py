fruits = 'apple,kiwi,mango'
fruit_list = list(fruits)
print(fruit_list)
print(len(fruit_list))

fruit_list = fruits.split(',')
print(fruit_list)

delimiter = ' | '
fruit_string = delimiter.join(fruit_list)
print(fruit_string)
