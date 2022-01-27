Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_dict = {}
>>> type(my_dict)
<class 'dict'>
>>> my_dict['bob'] = 2.5
>>> my_dict
{'bob': 2.5}
>>> my_dict['bob']
2.5
>>> my_dict['susie'] = 4.0
>>> my_dict['susie']
4.0
>>> my_dict['chimichumy']
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    my_dict['chimichumy']
KeyError: 'chimichumy'
>>> 
>>> 
>>> 
>>> 

>>> 
>>> my_dict
{'bob': 2.5, 'susie': 4.0}
>>> my_dict.keys()
dict_keys(['bob', 'susie'])
>>> my_dict.values()
dict_values([2.5, 4.0])
>>> my_dict.items()
dict_items([('bob', 2.5), ('susie', 4.0)])
>>> my_tup = ('bob',2.5)
>>> my_tup
('bob', 2.5)
>>> my_tup[0]
'bob'
>>> my_tup[1]
2.5
>>> my_tup[0] = 'bobby'
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    my_tup[0] = 'bobby'
TypeError: 'tuple' object does not support item assignment
>>> my_dict
{'bob': 2.5, 'susie': 4.0}
>>> my_tup
('bob', 2.5)
>>> name, gpa = my_tup
>>> 