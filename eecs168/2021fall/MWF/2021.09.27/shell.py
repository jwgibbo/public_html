Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> word = "the jello"
>>> word
'the jello'
>>> len(word)
9
>>> word[3]
' '
>>> str_to_list = list(word)
>>> str_to_list
['t', 'h', 'e', ' ', 'j', 'e', 'l', 'l', 'o']
>>> len(str_to_list)
9
>>> letters = ['a', 'b', 'c']
>>> letters
['a', 'b', 'c']
>>> list_to_str = str(letters)
>>> list_to_str
"['a', 'b', 'c']"
>>> print(letters)
['a', 'b', 'c']
>>> len(list_to_str)
15
>>> len(letters	)
3
>>> letters
['a', 'b', 'c']
>>> list_to_str = letters
>>> list_to_str
['a', 'b', 'c']
>>> list_to_str = ","
>>> list_to_str.join(letters)
'a,b,c'
>>> list_to_str
','
>>> list_to_str = list_to_str.join(letters)
>>> list_to_str
'a,b,c'
>>> len(list_to_str)
5
>>> list_to_str = " "
>>> list_to_str = list_to_str.join(letters)
>>> list_to_str
'a b c'
>>> len(list_to_str)
5
>>> list_to_str = ''
>>> list_to_str = list_to_str(letters)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    list_to_str = list_to_str(letters)
TypeError: 'str' object is not callable
>>> list_to_str = list_to_str.join(letter)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    list_to_str = list_to_str.join(letter)
NameError: name 'letter' is not defined
>>> list_to_str = list_to_str.join(letters)
>>> list_to_str
'abc'
>>> len(list_to_str)
3
>>> delimiter = ''
>>> letter_string = delimiter.join(letters)
>>> letter_string
'abc'
>>> "aaaaaBOOaaaaa"
'aaaaaBOOaaaaa'
>>> type("aaaaBOOaaaa")
<class 'str'>
>>> "aaaaaBOOaaaa".count("BOO")
1
>>> letter_string = ''.join(letter)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    letter_string = ''.join(letter)
NameError: name 'letter' is not defined
>>> letter_string = ''.join(letters)
>>> letter_string
'abc'
>>> delimter = ''
>>> letter_string = delimiter.join(letters)
>>> letter_string
'abc'
>>> word = "sandwich"
>>> list(word)
['s', 'a', 'n', 'd', 'w', 'i', 'c', 'h']
>>> word = "tuna fish sandwich"
>>> list(word)
['t', 'u', 'n', 'a', ' ', 'f', 'i', 's', 'h', ' ', 's', 'a', 'n', 'd', 'w', 'i', 'c', 'h']
>>> len( list(word) )
18
>>> order = word
>>> order
'tuna fish sandwich'
>>> order.split()
['tuna', 'fish', 'sandwich']
>>> order.split(" ")
['tuna', 'fish', 'sandwich']
>>> order = "tacos,drink,chips"
>>> order
'tacos,drink,chips'
>>> order.split(',')
['tacos', 'drink', 'chips']
>>> order
'tacos,drink,chips'
>>> order_as_list = order.split(',')
>>> order_as_list
['tacos', 'drink', 'chips']
>>> order_as_list[0]
'tacos'
>>> user_input = input("Type your name: ")
Type your name: John Gibbons
>>> user_input
'John Gibbons'
>>> 