Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_dict = {}
>>> type(my_dict)
<class 'dict'>
>>> my_dict['twix'] = 10
>>> my_dict
{'twix': 10}
>>> nums = [5, 10, 15]
>>> type(nums)
<class 'list'>
>>> my_dict[nums] = 'catfood'
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    my_dict[nums] = 'catfood'
TypeError: unhashable type: 'list'
>>> my_dict['m&ms'] = ['plain', 'peanut', 'mini', 'pretzel', 'carmel', 'brownie']
>>> my_dict
{'twix': 10, 'm&ms': ['plain', 'peanut', 'mini', 'pretzel', 'carmel', 'brownie']}
>>> len(my_dict)
2
>>> my_dict['m&ms']
['plain', 'peanut', 'mini', 'pretzel', 'carmel', 'brownie']
>>> len(my_dict['m&ms'])
6
>>> for candy in my_dict.keys():
	print(candy)

	
twix
m&ms
>>> nums
[5, 10, 15]
>>> my_dict
{'twix': 10, 'm&ms': ['plain', 'peanut', 'mini', 'pretzel', 'carmel', 'brownie']}
>>> my_dict.pop('twix')
10
>>> my_dict
{'m&ms': ['plain', 'peanut', 'mini', 'pretzel', 'carmel', 'brownie']}
>>> len(my_dict)
1
>>> type(my_dict['m&ms'])
<class 'list'>
>>> my_dict['m&ms'].remove('mini')
>>> my_dict['m&ms']
['plain', 'peanut', 'pretzel', 'carmel', 'brownie']
>>> type(my_dict.items())
<class 'dict_items'>
>>> my_tup = ('a', 1)
>>> type(my_tup)
<class 'tuple'>
>>> my_tup[0]
'a'
>>> my_tup[1]
1
>>> my_tup[0] = 'b'
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    my_tup[0] = 'b'
TypeError: 'tuple' object does not support item assignment
>>> letters = {'a': 1, 'b': 2, 'c': 3}
>>> type(letters)
<class 'dict'>
>>> for letter, num in letter.items():
	print(letter, num)

	
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    for letter, num in letter.items():
NameError: name 'letter' is not defined
>>> for letter, num in letters.items():
	print(letter, num)

	
a 1
b 2
c 3
>>> my_tup
('a', 1)
>>> letter, num = my_tup
>>> letter
'a'
>>> num
1
>>> names = ['homer', 'lisa', 'marge']
>>> for num, name in enumerate(names):
	print(num, name)

	
0 homer
1 lisa
2 marge
>>> 
