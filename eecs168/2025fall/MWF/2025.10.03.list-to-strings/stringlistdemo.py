word = 'cake'
word_as_list = list(word)
print(word)
print(word_as_list)
print(type(word))
print(type(word_as_list[0]))

fruits = 'apple,orange,kiwi'
fruits_list = fruits.split(',')
print(fruits_list)
print(len(fruits_list))

delimiter = '-'
hyphenated_fruits = delimiter.join(fruits_list)
print(hyphenated_fruits)
