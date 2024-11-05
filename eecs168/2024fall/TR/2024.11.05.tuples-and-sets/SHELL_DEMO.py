Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_tup = (5, 10, 15)
>>> my_tup
(5, 10, 15)
>>> a, b, c = my_tup
>>> a
5
>>> b
10
>>> c
15
>>> my_tup
(5, 10, 15)
>>> a, b = my_tup
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a, b = my_tup
ValueError: too many values to unpack (expected 2)
>>> a, b, c, d = my_tup
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a, b, c, d = my_tup
ValueError: not enough values to unpack (expected 4, got 3)
>>> a = my_tup
>>> my_tup
(5, 10, 15)
>>> a
(5, 10, 15)
>>> my_tup[0]
5
>>> my_tup[0] = 99
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    my_tup[0] = 99
TypeError: 'tuple' object does not support item assignment
>>> num_set = {5, 10, 15, 20, 25}
>>> num_set
{20, 5, 25, 10, 15}
>>> num_set[0]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    num_set[0]
TypeError: 'set' object is not subscriptable
>>> set_a = {5, 10, 15, 20}
>>> set_b = {25, 5, 30, 10}
>>> set_a.intersection(set_b)
{10, 5}
>>> set_a.union(set_b)
{5, 10, 15, 20, 25, 30}
>>> letters = set('banana')
>>> letters
{'a', 'b', 'n'}
>>> word1 = 'banana'
>>> word2 = 'barrage'
>>> set1 = set(word1)
>>> set1
{'a', 'b', 'n'}
>>> set2 = set(word2)
>>> set2
{'b', 'g', 'a', 'e', 'r'}
>>> set1.intersection(set2)
{'b', 'a'}
>>> set1.union(set2)
{'n', 'b', 'g', 'a', 'e', 'r'}
>>> set1.difference(set2)
{'n'}
>>> set2.difference(set1)
{'r', 'g', 'e'}
>>> words = ['bat', 'cat', 'sat', 'mat', 'cat', 'bat', 'mat', 'hat', 'map']
>>> words
['bat', 'cat', 'sat', 'mat', 'cat', 'bat', 'mat', 'hat', 'map']
>>> unique_words = set(words)
>>> unique_words
{'bat', 'cat', 'mat', 'map', 'hat', 'sat'}
>>> {[1,2,3]}
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    {[1,2,3]}
TypeError: unhashable type: 'list'
>>> 