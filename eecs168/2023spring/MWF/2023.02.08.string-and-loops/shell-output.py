Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> word = 'birthday'
>>> for letter in word:
	print(letter)

	
b
i
r
t
h
d
a
y
>>> word[3]
't'
>>> word[0]
'b'
>>> word[7]
'y'
>>> word[8]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    word[8]
IndexError: string index out of range
>>> len(word)
8
>>> word = 'cat'
>>> word[0]
'c'
>>> word[0] = 'b'
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    word[0] = 'b'
TypeError: 'str' object does not support item assignment
>>> word = 'birthday'
>>> word[0]
'b'
>>> word[5]
'd'
>>> word[0:5]
'birth'
>>> word[0:5:2]
'brh'
>>> word
'birthday'
>>> word[-1]
'y'
>>> word[-8]
'b'
>>> word[0:-8]
''
>>> word[-1:-9:-1]
'yadhtrib'
>>> word[::-1]
'yadhtrib'
>>> 
= RESTART: C:/Users/jwgibbo/Desktop/public_html/eecs168/2023spring/MWF/2023.02.08.string-and-loops/stringdemo.py
b
i
r
t
h
d
a
y
>>> 
= RESTART: C:/Users/jwgibbo/Desktop/public_html/eecs168/2023spring/MWF/2023.02.08.string-and-loops/stringdemo.py
b
i
r
t
h
d
a
y
======
b
i
r
t
h
d
a
y
>>> 
= RESTART: C:/Users/jwgibbo/Desktop/public_html/eecs168/2023spring/MWF/2023.02.08.string-and-loops/stringdemo.py
b
i
r
t
h
d
a
y
======
b
i
r
t
h
d
a
y
>>> 
= RESTART: C:/Users/jwgibbo/Desktop/public_html/eecs168/2023spring/MWF/2023.02.08.string-and-loops/stringdemo.py
b
i
r
t
h
d
a
y
======
0
1
2
3
4
5
6
7
>>> 
= RESTART: C:/Users/jwgibbo/Desktop/public_html/eecs168/2023spring/MWF/2023.02.08.string-and-loops/stringdemo.py
b
i
r
t
h
d
a
y
======
0 b
1 i
2 r
3 t
4 h
5 d
6 a
7 y
>>> 