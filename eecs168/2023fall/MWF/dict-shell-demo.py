Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> grades = {}
>>> type(grades)
<class 'dict'>
>>> grades['john'] = 63
>>> grades
{'john': 63}
>>> len(grades)
1
>>> grades['lisa'] = 99
>>> grades['chimichumi'] = 88
>>> grades
{'john': 63, 'lisa': 99, 'chimichumi': 88}
>>> len(grades)
3
>>> grades['lisa']
99
>>> grades.pop('chimichumi')
88
>>> grades
{'john': 63, 'lisa': 99}
>>> grades['john'] = 68
>>> gradeds
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    gradeds
NameError: name 'gradeds' is not defined
>>> grades
{'john': 68, 'lisa': 99}
>>> grades[john]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    grades[john]
NameError: name 'john' is not defined
>>> key = 'john'
>>> grades[key]
68
>>> grades[99]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    grades[99]
KeyError: 99
>>> key = 'sandwich'
>>> grades[key]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    grades[key]
KeyError: 'sandwich'
>>> grades[best_key]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    grades[best_key]
NameError: name 'best_key' is not defined
>>> spooky_movies = {}
>>> spooky_movies['Evil Dead'] = 10
>>> spooky_moveis['Monster House'] = 'TBD'
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    spooky_moveis['Monster House'] = 'TBD'
NameError: name 'spooky_moveis' is not defined
>>> spooky_movies['Monster House'] = 'TBD'
>>> spooky_movies['Monster House'] = 7
>>> spooky_movies['Monster House'] = 'TBD'
>>> spooky_movies['Scream'] = 7
>>> spooky_movies['Nightmare on Elm Street'] = 10
>>> spooky_movies
{'Evil Dead': 10, 'Monster House': 'TBD', 'Scream': 7, 'Nightmare on Elm Street': 10}
>>> for title in spooky_movies.keys():
	print(title)

	
Evil Dead
Monster House
Scream
Nightmare on Elm Street
>>> for rating in spooky_movies.values():
	print(rating)

	
10
TBD
7
10
>>> for title, rating in spooky_movies.items():
	print(title, '=', rating)

	
Evil Dead = 10
Monster House = TBD
Scream = 7
Nightmare on Elm Street = 10
>>> d1 = {'a':1}
>>> d2 = {'b':2}
>>> d1+d2
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    d1+d2
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> 