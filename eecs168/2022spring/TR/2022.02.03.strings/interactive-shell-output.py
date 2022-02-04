Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> while user_guess != 55:
	user_guess = int(input('Enter a guess: '))

	
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    while user_guess != 55:
NameError: name 'user_guess' is not defined
>>> word = 'groundhog'
>>> word
'groundhog'
>>> type(word)
<class 'str'>
>>> word[0]
'g'
>>> word[5]
'd'
>>> word[99]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    word[99]
IndexError: string index out of range
>>> word[-1]
'g'
>>> word[-2]
'o'
>>> word[-3]
'h'
>>> word[-10]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    word[-10]
IndexError: string index out of range
>>> word[-9]
'g'
>>> len(word)
9
>>> word = 'cat'
>>> len(word)
3
>>> word = 'ca'
>>> len(word)
2
>>> word = 'c'
>>> len(1)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    len(1)
TypeError: object of type 'int' has no len()
>>> len(word)
1
>>> word = ''
>>> type(word)
<class 'str'>
>>> len(word)
0
>>> word = ' '
>>> len(word)
1
>>> word = 'hi bob'
>>> len(word)
6
>>> word = 'groundhog'
>>> len(word)
9
>>> word[0:4]
'grou'
>>> word[0:9]
'groundhog'
>>> word[0:len(word)]
'groundhog'
>>> word[9]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    word[9]
IndexError: string index out of range
>>> word[0:9:2]
'gonhg'
>>> word[0:9:1]
'groundhog'
>>> word[-1]
'g'
>>> word[-2]
'o'
>>> word[-1:-4:-1]
'goh'
>>> word
'groundhog'
>>> 'g' in word
True
>>> 'r' in word
True
>>> 'z' in word
False
>>> 'G' in word
False
>>> 'hog' in word
True
>>> 'round' in word
True
>>> 'rh' in word
False
>>> my_slice = word[0:9:2]
>>> my_slice
'gonhg'
>>> word
'groundhog'
>>> 
