Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 2.5
>>> int(num)
2
>>> num = float("2.5")
>>> num
2.5
>>> type(num)
<class 'float'>
>>> print("I love " + str(num))
I love 2.5
>>> word = 'banana'
>>> word_as_list = list(word)
>>> word_as_list
['b', 'a', 'n', 'a', 'n', 'a']
>>> len(word_as_list)
6
>>> word_as_list[2]
'n'
>>> phrase = "How much snow do you think we'll get tomorrow?"
>>> phrase
"How much snow do you think we'll get tomorrow?"
>>> phrase_as_list = list(phrase)
>>> phrase_as_list
['H', 'o', 'w', ' ', 'm', 'u', 'c', 'h', ' ', 's', 'n', 'o', 'w', ' ', 'd', 'o', ' ', 'y', 'o', 'u', ' ', 't', 'h', 'i', 'n', 'k', ' ', 'w', 'e', "'", 'l', 'l', ' ', 'g', 'e', 't', ' ', 't', 'o', 'm', 'o', 'r', 'r', 'o', 'w', '?']
>>> phrase_as_list = phrase.split()
>>> phrase_as_list
['How', 'much', 'snow', 'do', 'you', 'think', "we'll", 'get', 'tomorrow?']
>>> len(phrase_as_list)
9
>>> groceries = 'bread,milk,toliet paper,uno'
>>> len(groceries)
27
>>> grocery_list = groceries.split(',')
>>> grocery_list
['bread', 'milk', 'toliet paper', 'uno']
>>> grocery_list = groceries.split([',
				
SyntaxError: EOL while scanning string literal
>>> grocery_list = groceries.split([',','t'])
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    grocery_list = groceries.split([',','t'])
TypeError: must be str or None, not list
>>> grocery_list = groceries.split(',', 2)
>>> grocery_list
['bread', 'milk', 'toliet paper,uno']
>>> nums = [1, 2, 3, 4]
>>> nums
[1, 2, 3, 4]
>>> nums_as_str = str(nums)
>>> nums_as_str
'[1, 2, 3, 4]'
>>> len(nums_as_str)
12
>>> print(nums)
[1, 2, 3, 4]
>>> delimeter = '
SyntaxError: EOL while scanning string literal
>>> delimeter = ','
>>> nums_as_str = delimeter.join(nums)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    nums_as_str = delimeter.join(nums)
TypeError: sequence item 0: expected str instance, int found
>>> nums
[1, 2, 3, 4]
>>> grocery_list
['bread', 'milk', 'toliet paper,uno']
>>> grocery_list = groceries.split(',')
>>> grocery_list
['bread', 'milk', 'toliet paper', 'uno']
>>> grocery_str = delimiter.join(grocery_list)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    grocery_str = delimiter.join(grocery_list)
NameError: name 'delimiter' is not defined
>>> grocery_str = delimeter.join(grocery_list)
>>> grocery_str
'bread,milk,toliet paper,uno'
>>> 