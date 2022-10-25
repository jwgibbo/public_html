Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> movies = {}
>>> movies['scream'] = 2000
>>> movies['american psycho'] = 2001
>>> movies['Nightmare on Elm'] = 1985
>>> movies['Halloween'] = 1978
>>> movies
{'scream': 2000, 'american psycho': 2001, 'Nightmare on Elm': 1985, 'Halloween': 1978}
>>> len(movies)
4
>>> movies.pop('Halloween')
1978
>>> movies
{'scream': 2000, 'american psycho': 2001, 'Nightmare on Elm': 1985}
>>> len(movies)
3
>>> movies.pop()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    movies.pop()
TypeError: pop expected at least 1 argument, got 0
>>> movies.popitem()
('Nightmare on Elm', 1985)
>>> movies
{'scream': 2000, 'american psycho': 2001}
>>> movies['Halloween']
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    movies['Halloween']
KeyError: 'Halloween'
>>> 'Halloween' in movies
False
>>> 'Halloween' in movies.keys()
False
>>> my_tup = ('a', 1)
>>> type(my_tup)
<class 'tuple'>
>>> my_tup[1]
1
>>> my_tup[0]
'a'
>>> my_tup[0:]
('a', 1)
>>> for elem in my_tup:
	print(elem)

	
a
1
>>> my_tup[0] = 'b'
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    my_tup[0] = 'b'
TypeError: 'tuple' object does not support item assignment
>>> my_tup
('a', 1)
>>> letter, num = my_tup
>>> my_tup
('a', 1)
>>> letter
'a'
>>> num
1
>>> movies
{'scream': 2000, 'american psycho': 2001}
>>> movies['hocus pocus'] = 1993
>>> movies
{'scream': 2000, 'american psycho': 2001, 'hocus pocus': 1993}
>>> type(movies)
<class 'dict'>
>>> for movie, year in movies.items():
	print(f'{movie} came out in {year}')

	
scream came out in 2000
american psycho came out in 2001
hocus pocus came out in 1993
>>> for movie, year in movies.items():
	print('{movie} came out in {year}')

	
{movie} came out in {year}
{movie} came out in {year}
{movie} came out in {year}
>>> for movie, year in movies.items():
	print(f'{movie} came out in {year}')

	
scream came out in 2000
american psycho came out in 2001
hocus pocus came out in 1993
>>> 