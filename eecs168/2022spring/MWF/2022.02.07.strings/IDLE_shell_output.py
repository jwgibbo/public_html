Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> word = 'cat'
>>> word
'cat'
>>> word[0]
'c'
>>> word[1]
'a'
>>> word[2]
't'
>>> word[3]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    word[3]
IndexError: string index out of range
>>> len(word)
3
>>> word[-1]
't'
>>> word[-4]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    word[-4]
IndexError: string index out of range
>>> word = 'valentine'
>>> word[0:4]
'vale'
>>> len(word)
9
>>> word[0:9]
'valentine'
>>> len(word)
9
>>> word[0:9:2]
'vlnie'
>>> word[2:5]
'len'
>>> word[2:7:3]
'lt'
>>> 'v' in word
True
>>> 'V' in word
False
>>> 'len' in word
True
>>> 'lne' in word
False
>>> word[-1:-9:-1]
'enitnela'
>>> word[-1:-10:-1]
'enitnelav'
>>> word[2:8:-2]
''
>>> word[2:8:2]
'lni'
>>> word[8:2:2]
''
>>> word[8:2:-2]
'ein'
>>> 