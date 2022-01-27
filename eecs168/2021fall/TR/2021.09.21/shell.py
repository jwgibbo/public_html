Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> word = "doggy"
>>> word
'doggy'
>>> word[2]
'g'
>>> word[1:4]
'ogg'
>>> word.count("BOO")
0
>>> word.count("dog")
1
>>> len(word)
5
>>> "dog" in word
True
>>> "BOO" in word
False
>>> word[0:3].count('d')
1
>>> word
'doggy'
>>> word = word + '!'
>>> word
'doggy!'
>>> word[0] = 'L'
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    word[0] = 'L'
TypeError: 'str' object does not support item assignment
>>> word = "Loggy!"
>>> word
'Loggy!'
>>> 
>>> 
>>> 
>>> 
>>> nums = [2, 3, 5, 8]
>>> nums
[2, 3, 5, 8]
>>> nums[0]
2
>>> nums[3] = 7
>>> nums
[2, 3, 5, 7]
>>> word = "Loggy!"
>>> word[0] = 'd'
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    word[0] = 'd'
TypeError: 'str' object does not support item assignment
>>> nums = [2,3,5,7]
>>> nums
[2, 3, 5, 7]
>>> type('d')
<class 'str'>
>>> type('dddddddddddddddd')
<class 'str'>
>>> type(word[0])
<class 'str'>
>>> word[0] = 'dddddddddddd'
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    word[0] = 'dddddddddddd'
TypeError: 'str' object does not support item assignment
>>> greetings = ['hi', 'hola', 'bonjour', 'hallo', 'salam']
>>> greetings[0]
'hi'
>>> groceries = ['bread', 'milk']
>>> 
= RESTART: H:/public_html/eecs168/2021fall/TR/2021.09.21/lists-intro.py
hi
hola
bonjour
hallo
salam
>>> 'milk' in groceries
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    'milk' in groceries
NameError: name 'groceries' is not defined
>>> groceries = ['bread', 'milk']
>>> groceries
['bread', 'milk']
>>> 'milk' in groceries
True
>>> 'juice' in groceries
False
>>> nums
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    nums
NameError: name 'nums' is not defined
>>> nums = [2,3,5,7]
>>> nums
[2, 3, 5, 7]
>>> nums[0:3]
[2, 3, 5]
>>> groceries
['bread', 'milk']
>>> groceries.append('eggs')
>>> groceries
['bread', 'milk', 'eggs']
>>> int(2.5)
2
>>> list(5)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    list(5)
TypeError: 'int' object is not iterable
>>> list("banana")
['b', 'a', 'n', 'a', 'n', 'a']
>>> list(range(1,10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> banana_list = list("banana")
>>> banana_list
['b', 'a', 'n', 'a', 'n', 'a']
>>> print(banana_list)
['b', 'a', 'n', 'a', 'n', 'a']
>>> str(banana_list)
"['b', 'a', 'n', 'a', 'n', 'a']"
>>> print(5.2)
5.2
>>> str(5.2)
'5.2'
>>> nums
[2, 3, 5, 7]
>>> nums = nums + 11
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    nums = nums + 11
TypeError: can only concatenate list (not "int") to list
>>> nums.append(11)
>>> nums
[2, 3, 5, 7, 11]
>>> nums = nums + [13]
>>> nums
[2, 3, 5, 7, 11, 13]
>>> greeting
'salam'
>>> greetings
['hi', 'hola', 'bonjour', 'hallo', 'salam']
>>> greetings[2]
'bonjour'
>>> greetings[2][0]
'b'
>>> greetings[2][0:3]
'bon'
>>> 