Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_tup = ('bob',95)
>>> my_tup
('bob', 95)
>>> my_tup[0]
'bob'
>>> my_tup[1]
95
>>> my_tup[2]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    my_tup[2]
IndexError: tuple index out of range
>>> my_tup[0] = 'bobby'
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    my_tup[0] = 'bobby'
TypeError: 'tuple' object does not support item assignment
>>> candies = {}
>>> candies['almond joy'] = 10
>>> candies
{'almond joy': 10}
>>> candies['skittles'] = 6.5
>>> candies
{'almond joy': 10, 'skittles': 6.5}
>>> candies['snickers'] = 3
>>> candies
{'almond joy': 10, 'skittles': 6.5, 'snickers': 3}
>>> candies.keys()
dict_keys(['almond joy', 'skittles', 'snickers'])
>>> candies.values()
dict_values([10, 6.5, 3])
>>> candies.items()
dict_items([('almond joy', 10), ('skittles', 6.5), ('snickers', 3)])
>>> for elem in candies:
	print(elem)

	
almond joy
skittles
snickers
>>> for key, value in candies:
	print(f"{key} rating: {value}")

	
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    for key, value in candies:
ValueError: too many values to unpack (expected 2)
>>> for key, value in candies.items():
	print(f"{key} rating: {value}")

	
almond joy rating: 10
skittles rating: 6.5
snickers rating: 3
>>> for candy, rating in candies.items():
	print(candy + " rating : " + rating)

	
Traceback (most recent call last):
  File "<pyshell#26>", line 2, in <module>
    print(candy + " rating : " + rating)
TypeError: can only concatenate str (not "int") to str
>>> for candy, rating in candies.items():
	print(candy + " rating : " + str(rating))

	
almond joy rating : 10
skittles rating : 6.5
snickers rating : 3
>>> 