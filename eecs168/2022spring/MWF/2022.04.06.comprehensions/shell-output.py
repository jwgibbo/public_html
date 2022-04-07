Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> winrar = [2008, 2022, 1988, 1923]
>>> win_dict = {year : 'champion'  for year in winrar}
>>> win_dict
{2008: 'champion', 2022: 'champion', 1988: 'champion', 1923: 'champion'}
>>> win_dict[2008]
'champion'
>>> win_dict[2022]
'champion'
>>> win_dict[2021]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    win_dict[2021]
KeyError: 2021
>>> results = [(2008, 'champion'), (2022, 'champion'), (1988, 'champion'), (2020, 'COVID'), (2021, 'sweet 16'), (2018, 'final four')]
>>> result
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    result
NameError: name 'result' is not defined
>>> results
[(2008, 'champion'), (2022, 'champion'), (1988, 'champion'), (2020, 'COVID'), (2021, 'sweet 16'), (2018, 'final four')]
>>> type(results)
<class 'list'>
>>> type(results[0])
<class 'tuple'>
>>> results[2018]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    results[2018]
IndexError: list index out of range
>>> results_dict = {year : result for year, result in results}
>>> results_dict[2018]
'final four'
>>> result_dict[2022]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    result_dict[2022]
NameError: name 'result_dict' is not defined
>>> results_dict[2022]
'champion'
>>> results_dict[2020]
'COVID'
>>> results_dict = {}
>>> for year, result in results:
	results[year] = result

	
Traceback (most recent call last):
  File "<pyshell#20>", line 2, in <module>
    results[year] = result
IndexError: list assignment index out of range
>>> for year, result in results:
	results_dict[year] = result

	
>>> results_dict
{2008: 'champion', 2022: 'champion', 1988: 'champion', 2020: 'COVID', 2021: 'sweet 16', 2018: 'final four'}
>>> my_tup = ('cat', 'hat', 'bat')
>>> animal1, animal2, animal3 = my_tup
>>> animal1
'cat'
>>> nums = [1,2,3,4,5]
>>> for a, b in nums:
	print(a)
	print(b)

	
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    for a, b in nums:
TypeError: cannot unpack non-iterable int object
>>> phrase = "The film 'Jaws' is the best film!"
>>> my_set = set()
>>> for letter in phrase:
	my_set.add(letter)

	
>>> my_set
{' ', 't', "'", 'e', 'h', 'w', 'm', '!', 'J', 'f', 'a', 'l', 's', 'b', 'T', 'i'}
>>> vowels = {}
>>> type(vowels)
<class 'dict'>
>>> vowels = {letter for letter in phrase if letter.lower() in 'aeiou'}
\
>>> vowels
{'a', 'e', 'i'}
>>> quit()
>>> words = 'hat bat cat sat'
>>> words
'hat bat cat sat'
>>> words.split()
['hat', 'bat', 'cat', 'sat']
>>> a, b, c, d = words.split()
>>> a
'hat'
>>> b
'bat'
>>> c
'cat'
>>> d
'sat'
>>> 