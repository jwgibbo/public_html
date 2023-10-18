Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_tup = (5, 10, 15)
>>> type(my_tup)
<class 'tuple'>
>>> my_tup[0]
5
>>> len(my_tup)
3
>>> for num in my_tup:
	print(num)

	
5
10
15
>>> my_tup[0] = 99
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    my_tup[0] = 99
TypeError: 'tuple' object does not support item assignment
>>> key = ('john', 'gibbons')
>>> my_dict = {}
>>> my_dict[key] = 'oct 3rd'
>>> my_dict
{('john', 'gibbons'): 'oct 3rd'}
>>> my_tup
(5, 10, 15)
>>> num1, num2, num3 = my_tup
>>> num1
5
>>> num2
10
>>> num3
15
>>> for key, value in my_dict.items():
	print('key =', key, 'value =', value)

	
key = ('john', 'gibbons') value = oct 3rd
>>> my_tup
(5, 10, 15)
>>> num1, num2 = my_tup
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    num1, num2 = my_tup
ValueError: too many values to unpack (expected 2)
>>> num1, num2 = my_tup[0:2]
>>> num1
5
>>> num2
10
>>> letters = set('banana')
>>> letters
{'n', 'b', 'a'}
>>> letters[0]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    letters[0]
TypeError: 'set' object is not subscriptable
>>> banana_set = set('banana')
>>> bandana_set = set('bandana')
>>> banana_set.intersection(bandana_set)
{'n', 'b', 'a'}
>>> bandana_set.union(banana_set)
{'d', 'a', 'n', 'b'}
>>> bandana_set.union(banana_set)
{'d', 'a', 'n', 'b'}
>>> my_set = {5, 10, 15}
>>> a,b,c = my_set
>>> a
10
>>> b
5
>>> c
15
>>> bandana_set.difference(banana_set)
{'d'}
>>> banana_set.difference(bandana_set)
set()
>>> 