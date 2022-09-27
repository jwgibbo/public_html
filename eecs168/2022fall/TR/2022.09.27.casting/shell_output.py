Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> cereal = 'count chocula'
>>> len(cereal)
13
>>> cereal_list = list(cereal)
>>> cereal_list
['c', 'o', 'u', 'n', 't', ' ', 'c', 'h', 'o', 'c', 'u', 'l', 'a']
>>> len(cereal_list)
13
>>> letters = ['c', 'a', 't']
>>> len(letters)
3
>>> letters_string = str(letters)
>>> len(letter_string)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    len(letter_string)
NameError: name 'letter_string' is not defined
>>> len(letters_string)
15
>>> letters_string
"['c', 'a', 't']"
>>> letters
['c', 'a', 't']
>>> delimiter = ','
>>> delimiter.join(letters)
'c,a,t'
>>> delimiter = ''
>>> delimiter.join(letters)
'cat'
>>> cereal
'count chocula'
>>> list(cereal)
['c', 'o', 'u', 'n', 't', ' ', 'c', 'h', 'o', 'c', 'u', 'l', 'a']
>>> cereal.split(' ')
['count', 'chocula']
>>> cereal.split('')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    cereal.split('')
ValueError: empty separator
>>> cereal.split()
['count', 'chocula']
>>> 