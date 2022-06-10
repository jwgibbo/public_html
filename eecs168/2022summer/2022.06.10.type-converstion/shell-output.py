Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5+3
8
>>> "abc" + "def"
'abcdef'
>>> print("abc", "def")
abc def
>>> print("abc"+"def")
abcdef
>>> 'abc','def'
('abc', 'def')
>>> letters = 'abc' + 'def'
>>> letters
'abcdef'
>>> type(letters)
<class 'str'>
>>> letters = 'abc', 'def'
>>> letters
('abc', 'def')
>>> type(letters)
<class 'tuple'>
>>> print(5+3)
8
>>> 5+3
8
>>> 3+5
8
>>> 'abc'+'def'
'abcdef'
>>> 'def'+'abc'
'defabc'
>>> 'I love ' + 'bananas!'
'I love bananas!'
>>> 'ha'*3
'hahaha'
>>> 'ha'*0
''
>>> 'ha'*-1
''
>>> 'abc'*'cat'
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    'abc'*'cat'
TypeError: can't multiply sequence by non-int of type 'str'
>>> 'ab'*2.5
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    'ab'*2.5
TypeError: can't multiply sequence by non-int of type 'float'
>>> 5+5
10
>>> 5+'5'
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    5+'5'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> int('562')
562
>>> int('562') + 1
563
>>> int(3.14159265358979323)
3
>>> 5/2
2.5
>>> int(5/2)
2
>>> 5//2
2
>>> float('3.14159')
3.14159
>>> float(2)
2.0
>>> type(2)
<class 'int'>
>>> type(2.0)
<class 'float'>
>>> str(42)
'42'
>>> str(3.14159)
'3.14159'
>>> float('rootbeer')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    float('rootbeer')
ValueError: could not convert string to float: 'rootbeer'
>>> int('5+2')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    int('5+2')
ValueError: invalid literal for int() with base 10: '5+2'
>>> int('5'+'2')
52
>>> int('2.5')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    int('2.5')
ValueError: invalid literal for int() with base 10: '2.5'
>>> first_name = "John"
>>> 1st_name = "John"
SyntaxError: invalid syntax
>>> x = 5
>>> 5 = 9
SyntaxError: cannot assign to literal
>>> 