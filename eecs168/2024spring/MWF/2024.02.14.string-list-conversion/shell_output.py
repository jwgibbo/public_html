Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
word = 'titanic'
nums = [27, 13, 99, 55, 101]
word[4]
'n'
nums[4]
101
nums[0:3:1]
[27, 13, 99]
nums
[27, 13, 99, 55, 101]
nums = nums[0:3:1]
nums
[27, 13, 99]
[1,2,3]+[4,5,6]
[1, 2, 3, 4, 5, 6]
nums = nums + [55, 101]
nums
[27, 13, 99, 55, 101]
word[-4]
'a'
word[4]
'n'
nums[-1]
101
word
'titanic'
word[-1:-8:-1]
'cinatit'
word[::-1]
'cinatit'
nums[::-1]
[101, 55, 99, 13, 27]
nums = 'catfood'
nums
'catfood'
nums = [101, 55, 99, 13, 27]
nums
[101, 55, 99, 13, 27]
nums[3] = 888
nums
[101, 55, 99, 888, 27]
>>> word
'titanic'
>>> word[0] = 'j'
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    word[0] = 'j'
TypeError: 'str' object does not support item assignment
>>> word = 3.14
>>> word = 'titanic'
>>> type(word)
<class 'str'>
>>> word = 3.14
>>> type(word)
<class 'float'>
>>> word = 'titanic'
>>> word[0] = 'j'
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    word[0] = 'j'
TypeError: 'str' object does not support item assignment
>>> word.count('t')
2
>>> nums.count(55)
1
>>> word.upper()
'TITANIC'
>>> nums.upper()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    nums.upper()
AttributeError: 'list' object has no attribute 'upper'
float('3.14')
3.14
type(nums)
<class 'list'>
word
'titanic'
word_as_list = list(word)
word_as_list
['t', 'i', 't', 'a', 'n', 'i', 'c']
len(word_as_list)
7
groceries = ['ramen', 'peanuts', 'sesame oil', 'red pepper flakes', 'furikake']
groceries = 'ramen,peanuts,sesame oil,red pepper flakes,furikake'
len(groceries)
51
grocery_list = list(groceries)
grocery_list
['r', 'a', 'm', 'e', 'n', ',', 'p', 'e', 'a', 'n', 'u', 't', 's', ',', 's', 'e', 's', 'a', 'm', 'e', ' ', 'o', 'i', 'l', ',', 'r', 'e', 'd', ' ', 'p', 'e', 'p', 'p', 'e', 'r', ' ', 'f', 'l', 'a', 'k', 'e', 's', ',', 'f', 'u', 'r', 'i', 'k', 'a', 'k', 'e']
grocery_list = groceries.split(',')
len(grocery_list)
5
grocery_list
['ramen', 'peanuts', 'sesame oil', 'red pepper flakes', 'furikake']

colors = ['yellow', 'teal', 'turquiose', 'orange']
str(colors)
"['yellow', 'teal', 'turquiose', 'orange']"
len(str(colors))
41
len(str(['a','b','c']))
15
str(['a','b','c'])
"['a', 'b', 'c']"
delimiter = '$'
delimeter = '$'
color_string = delimeter.join(colors)
color_string
'yellow$teal$turquiose$orange'
delimeter = '-----'
color_string = delimeter.join(colors)
color_string
'yellow-----teal-----turquiose-----orange'
