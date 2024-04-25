Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 'A' if 5<10 else 'B'
'A'
>>> 'A' if 5>10 else 'B'
'B'
>>> nums = [5, 10, 15, 20]
>>> doubles = [num*2 for num in nums]
>>> double
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    double
NameError: name 'double' is not defined. Did you mean: 'doubles'?
>>> doubles
[10, 20, 30, 40]
>>> odds = [num for num in nums if num%2 != 0]
>>> odds
[5, 15]
>>> nums
[5, 10, 15, 20]
>>> if 'cat':
...     print('this worked?')
... 
...     
this worked?
>>> if '':
...     print('it is true')
... else:
...     print('it is false')
... 
...     
it is false
if 0:
    print('it is true')
else:
    print('it is false')

    
it is false
if 1:
    print('it is true')
else:
    print('it is false')

    
it is true
if 55:
    print('it is true')
else:
    print('it is false')

    
it is true
'catfood'%2
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    'catfood'%2
TypeError: not all arguments converted during string formatting
x = if True:
    
SyntaxError: invalid syntax

x = 1 if True else 2
x
1
nums
[5, 10, 15, 20]
5 if True else 10
5
nums
[5, 10, 15, 20]





numns
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    numns
NameError: name 'numns' is not defined. Did you mean: 'nums'?
byn
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    byn
NameError: name 'byn' is not defined. Did you mean: 'bin'?
nums
[5, 10, 15, 20]
4%2
0
0%2
0
squbes = [num**3 if num%2==0 else num**2 for num in nums]

squbes
[25, 1000, 225, 8000]
nums = [3, 5, 15, 2, 9, 7, 30]
['fizzbuzz' if num%3==0 and num%5==0 else 'fizz' if num%3==0 else 'buzz' for num in nums if num%3==0 or num%5==0]
['fizz', 'buzz', 'fizzbuzz', 'fizz', 'fizzbuzz']
['fizz' if num%3==0 else 'fizzbuzz' if num%3==0 and num%5==0 else 'buzz' for num in nums if num%3==0 or num%5==0]
['fizz', 'buzz', 'fizz', 'fizz', 'fizz']
['fizzbuzz' if num%3==0 and num%5==0 else 'fizz' if num%3==0 else 'buzz' for num in nums if num%3==0 or num%5==0]
['fizz', 'buzz', 'fizzbuzz', 'fizz', 'fizzbuzz']
[('fizz' if num%3==0 else '')+('buzz' if num%5==0 else '') for num in nums if num%3==0 or num%5==0]
['fizz', 'buzz', 'fizzbuzz', 'fizz', 'fizzbuzz']
[('fizz' if num%3==0 else )+('buzz' if num%5==0 else '') for num in nums if num%3==0 or num%5==0]
SyntaxError: invalid syntax
