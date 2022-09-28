Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> animals = 'cat bat rat'
>>> list(animals)
['c', 'a', 't', ' ', 'b', 'a', 't', ' ', 'r', 'a', 't']
>>> len(list(animals))
11
>>> letters = ['c', 'a', 't']
>>> len(letters)
3
>>> len(str(letters))
15
>>> str(letters)
"['c', 'a', 't']"
>>> animals
'cat bat rat'
>>> animals.split(' ')
['cat', 'bat', 'rat']
>>> animals
'cat bat rat'
>>> delimiter = ' '
>>> animals.split(delimiter)
['cat', 'bat', 'rat']
>>> letters
['c', 'a', 't']
>>> delimiter = ','
>>> delimiter.join(letters)
'c,a,t'
>>> delimiter = ''
>>> delimiter.join(letters)
'cat'
>>> letters_str = delimiter.join(letters)
>>> len(letters_str)
3
>>> letters_str
'cat'
>>> food = 'HAM'
>>> food.join(letters)
'cHAMaHAMt'
>>> food
'HAM'
>>> weird_ham_str = food.join(letters)
>>> weird_ham_str
'cHAMaHAMt'
>>> 