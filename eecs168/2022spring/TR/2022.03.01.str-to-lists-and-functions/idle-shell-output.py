Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> word = 'buffet'
>>> word
'buffet'
>>> int(5.5)
5
>>> str(123)
'123'
>>> float("3.14")
3.14
>>> list(4)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(4)
TypeError: 'int' object is not iterable
>>> word_as_list = list(word)
>>> word_as_list
['b', 'u', 'f', 'f', 'e', 't']
>>> len(word)
6
>>> len(word_as_list)
6
>>> word = str(word_as_list)
>>> word
"['b', 'u', 'f', 'f', 'e', 't']"
>>> len(word)
30
>>> print(word_as_list)
['b', 'u', 'f', 'f', 'e', 't']
>>> phrase = "Today is Mardi Gras"
>>> phrase_as_list = list(phrase)
>>> phrase_as_list
['T', 'o', 'd', 'a', 'y', ' ', 'i', 's', ' ', 'M', 'a', 'r', 'd', 'i', ' ', 'G', 'r', 'a', 's']
>>> phrase_as_list = phrase.split(' ')
>>> phrase_as_list
['Today', 'is', 'Mardi', 'Gras']
>>> phrase_as_list = phrase.split()
>>> phrase_as_list
['Today', 'is', 'Mardi', 'Gras']
>>> groceries = 'eggs,cheez-its,chicken,rice,disco fries'
>>> groceries
'eggs,cheez-its,chicken,rice,disco fries'
>>> grocery_list = groceries.split(',')
>>> grocery_list
['eggs', 'cheez-its', 'chicken', 'rice', 'disco fries']
>>> delimeter = '!'
>>> groceries = delimeter.join(grocery_list)
>>> groceries
'eggs!cheez-its!chicken!rice!disco fries'
>>> delimeter = 'QUACK'
>>> groceries = delimeter.join(grocery_list)
>>> groceries
'eggsQUACKcheez-itsQUACKchickenQUACKriceQUACKdisco fries'
>>> delimeter = '\n'
>>> groceries = delimeter.join(grocery_list)
>>> groceries
'eggs\ncheez-its\nchicken\nrice\ndisco fries'
>>> print(groceries)
eggs
cheez-its
chicken
rice
disco fries
>>> delimeter = ''
>>> groceries = delimeter.join(grocery_list)
>>> groceries
'eggscheez-itschickenricedisco fries'
>>> nums = [1,2,3,4]
>>> 3 in nums
True
>>> 