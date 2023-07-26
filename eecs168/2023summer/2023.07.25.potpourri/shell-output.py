Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'A' if True else 'B'
'A'
result = 'A' if True else 'B'
result = if True:
    
SyntaxError: invalid syntax
'A' if False else 'B'
'B'
x = 10
y = 20
'A' if (x+10) == (400%y) else 'B'
'B'
age = 15
if age > 21:
    ouput = 'Welcome'
else:
    output = 'Scram'

    
output
'Scram'
output = 'Welcome' if age > 21 else 'Scram'
output
'Scram'
>>> nums = list(range(5, 26, 1))
>>> nums
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
>>> cubes_of_5s = [num for num in nums if num%5==0]
>>> cubes_of_5s
[5, 10, 15, 20, 25]
>>> cubes_of_5s = [num**3 for num in nums if num%5==0]
>>> cubes_of_5s
[125, 1000, 3375, 8000, 15625]
>>> cubes_of_5s = ['taco' for num in nums if num%5==0]
>>> cubes_of_5s
['taco', 'taco', 'taco', 'taco', 'taco']
>>> cubes_of_5s_squares_of_10s = [num**2 if num%10==0 else num**3 for num in nums if num%5==0]
>>> 'A' if False else 'B' if True else 'C'
'B'
>>> 'A' if 5>10 else 'B' if '?'=='$' else 'C'
'C'
>>> age = -5
>>> output = 'Welcome' if age >= 21 else 'Scram' if age >= 0 else 'Invalid age!'
>>> ouput
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    ouput
NameError: name 'ouput' is not defined. Did you mean: 'output'?
>>> output
'Invalid age!'
num = 1
while True:
    print(num)
    if num > 3:
        break
    num += 1

    
1
2
3
4
num
4
