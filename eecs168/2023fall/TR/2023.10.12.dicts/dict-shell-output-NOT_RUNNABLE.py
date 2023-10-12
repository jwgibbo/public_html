Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> grades = {}
>>> type(grades)
<class 'dict'>
>>> grades['john'] = 62
>>> grades['lista'] = 99
>>> grades['chimichumi'] = 75
>>> grades
{'john': 62, 'lista': 99, 'chimichumi': 75}
>>> len(grades)
3
>>> grades['john']
62
>>> key = 'john'
>>> grades[key]
62
>>> print(grades['bob'])
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(grades['bob'])
KeyError: 'bob'
>>> spooky_films = {}
>>> spooky_films['Scream'] = 6.5
>>> spooky_films['Nightmare Before Christmas'] = 8
>>> spooky_films['The Shining'] = 9.5
>>> spooky_films['Monster House'] = 'TBD'
>>> spooky_films
{'Scream': 6.5, 'Nightmare Before Christmas': 8, 'The Shining': 9.5, 'Monster House': 'TBD'}
>>> len(spooky_films)
4
>>> for title in spooky_films.keys():
	print(title)

	
Scream
Nightmare Before Christmas
The Shining
Monster House
>>> for rating in spooky_films.values():
	print(rating)

	
6.5
8
9.5
TBD
>>> for title, rating in spooky_films.items():
	print(title, '=', rating)

	
Scream = 6.5
Nightmare Before Christmas = 8
The Shining = 9.5
Monster House = TBD
>>> spooky_film['Friday the 13th: Part VIII'] = 8
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    spooky_film['Friday the 13th: Part VIII'] = 8
NameError: name 'spooky_film' is not defined
>>> spooky_films['Friday the 13th: Part VIII'] = 8
>>> spooky_films
{'Scream': 6.5, 'Nightmare Before Christmas': 8, 'The Shining': 9.5, 'Monster House': 'TBD', 'Friday the 13th: Part VIII': 8}
>>> spooky_films['Scream'] = 6.6
>>> spooky_films
{'Scream': 6.6, 'Nightmare Before Christmas': 8, 'The Shining': 9.5, 'Monster House': 'TBD', 'Friday the 13th: Part VIII': 8}
>>> True or print('hi')
True
>>> def func():
	print('hi')
	return True

>>> func()
hi
True
>>> True or func()
True
>>> print('The above example with or was just a question; it does not pertain to dicts')
The above example with or was just a question; it does not pertain to dicts
>>> 'Scream' in spooky_films.keys()
True
>>> 'Scream' in spooky_films
True
>>> spooky_films
{'Scream': 6.6, 'Nightmare Before Christmas': 8, 'The Shining': 9.5, 'Monster House': 'TBD', 'Friday the 13th: Part VIII': 8}
>>> 'Halloween' in spooky_films
False
>>> 