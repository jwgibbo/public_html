Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> letters = set('bananramashamalama')
>>> letters
{'h', 'm', 'n', 's', 'a', 'r', 'l', 'b'}
>>> letters = set('bananas')
>>> letters
{'s', 'b', 'a', 'n'}
>>> len(letters)
4
>>> letters.add('z')
>>> letters
{'n', 's', 'a', 'z', 'b'}
>>> letters.add('p')
>>> letters
{'n', 's', 'a', 'p', 'z', 'b'}
>>> letters = set('bananas')
>>> letters
{'s', 'b', 'a', 'n'}
>>> letters
{'s', 'b', 'a', 'n'}
>>> letters.remove('b')
>>> letters
{'s', 'a', 'n'}
>>> letters.remove('z')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    letters.remove('z')
KeyError: 'z'
>>> letters[0]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    letters[0]
TypeError: 'set' object is not subscriptable
>>> my_likes = {'halloween', 'stardew valley', 'mayo'}
>>> your_likes = {'halloween', 'mayo', 'bbq', 'ketchup', 'ranch'}
>>> my_likes.intersection(your_likes)
{'mayo', 'halloween'}
>>> your_likes.intersection(my_likes)
{'mayo', 'halloween'}
>>> my_likes.difference(your_likes)
{'stardew valley'}
>>> your_likes.difference(my_likes)
{'ketchup', 'bbq', 'ranch'}
>>> random.randint(1, 6)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    random.randint(1, 6)
NameError: name 'random' is not defined
>>> import random
>>> random.randint(1, 6)
3
>>> random.randint(1, 6)
3
>>> random.randint(1, 6)
4
>>> random.randint(1, 6)
1
>>> random.randint(1, 6)
6
>>> random.randint(1, 6)
1
>>> random.randint(1, 6)
6
>>> random.randint(1, 6)
6
>>> random.randint(1, 6)
6
>>> random.randint(1, 6)
1
>>> random.randint(1, 6)
5
>>> random.randint(1, 20)
10
>>> random.randint(1, 20)
6
>>> dips = ['ketchup', 'bbq', 'ranch', 'mayo', 'mustard', 'cain\'s sauce', 'hot sauce']
>>> random.choice(dips)
"cain's sauce"
>>> random.choice(dips)
'mustard'
>>> len(dips)
7
>>> random.choices(dips, k=3)
['mayo', 'hot sauce', 'bbq']
>>> random.choices(dips, k=3)
['mustard', "cain's sauce", 'bbq']
>>> random.choices(dips, k=3)
['mayo', "cain's sauce", 'bbq']
>>> random.choices(dips, k=3)
['mustard', 'ranch', 'mayo']
>>> random.choices(dips, k=3)
["cain's sauce", 'hot sauce', 'mustard']
>>> random.choices(dips, k=3)
['ranch', 'mayo', 'hot sauce']
>>> random.choices(dips, k=3)
['hot sauce', 'hot sauce', 'hot sauce']
>>> random.choices(dips, k=30)
["cain's sauce", "cain's sauce", 'ketchup', 'ranch', 'bbq', 'mustard', 'mayo', "cain's sauce", 'hot sauce', "cain's sauce", 'ketchup', 'ketchup', 'ketchup', 'mayo', 'bbq', 'ketchup', 'mayo', 'ranch', 'mustard', "cain's sauce", 'hot sauce', 'hot sauce', "cain's sauce", 'hot sauce', 'ketchup', 'hot sauce', 'mayo', 'hot sauce', "cain's sauce", 'ranch']
>>> random.sample(dips, k=3)
["cain's sauce", 'hot sauce', 'mustard']
>>> random.sample(dips, k=3)
['ranch', "cain's sauce", 'ketchup']
>>> random.sample(dips, k=3)
['ketchup', 'ranch', 'hot sauce']
>>> random.sample(dips, k=3)
["cain's sauce", 'hot sauce', 'ranch']
>>> random.sample(dips, k=3)
['ranch', 'bbq', 'hot sauce']
>>> random.sample(dips, k=3)
["cain's sauce", 'mayo', 'ketchup']
>>> random.sample(dips, k=3)
['hot sauce', 'ranch', 'mayo']
>>> random.sample(dips, k=3)
['bbq', "cain's sauce", 'mayo']
>>> random.sample(dips, k=3)
['mayo', 'hot sauce', "cain's sauce"]
>>> random.sample(dips, k=3)
['mustard', 'bbq', 'mayo']
>>> random.sample(dips, k=3)
['ranch', 'ketchup', "cain's sauce"]
>>> random.sample(dips, k=30)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    random.sample(dips, k=30)
  File "C:\Program Files\Python39\lib\random.py", line 449, in sample
    raise ValueError("Sample larger than population or is negative")
ValueError: Sample larger than population or is negative
>>> dips
['ketchup', 'bbq', 'ranch', 'mayo', 'mustard', "cain's sauce", 'hot sauce']
>>> random.shuffle(dips)
>>> dips
['ranch', 'mayo', 'bbq', 'hot sauce', 'ketchup', "cain's sauce", 'mustard']
>>> 