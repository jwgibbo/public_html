Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_range = range(1, 5)
>>> my_range
range(1, 5)
>>> type(my_range)
<class 'range'>
>>> my_range[0]
1
>>> my_range[0] = 55
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    my_range[0] = 55
TypeError: 'range' object does not support item assignment
>>> my_range = range(3, 33, 3)
>>> for num in my_range:
	print(num)

	
3
6
9
12
15
18
21
24
27
30
>>> my_range = range(1, 5)
>>> for num in my_range:
	print(num)

	
1
2
3
4
>>> word = 'abcdefg'
>>> word[0:3]
'abc'
>>> my_range = range(3, 34, 3)
>>> for num in my_range:
	print(num)

	
3
6
9
12
15
18
21
24
27
30
33
>>> my_range = range(5)
>>> for num in my_range:
	print(num)

	
0
1
2
3
4
>>> my_range = range(-10, 11)
>>> for num in my_range:
	print(num)

	
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
0
1
2
3
4
5
6
7
8
9
10
>>> my_range = range(-10)
>>> for num in my_range:
	print(num)

	
>>> my_range = range(-10, -20, -2)
>>> for num in my_range:
	print(num)

	
-10
-12
-14
-16
-18
>>> my_range = range(0, 1, .1)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    my_range = range(0, 1, .1)
TypeError: 'float' object cannot be interpreted as an integer
>>> my_range = range(0, 10, 0)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    my_range = range(0, 10, 0)
ValueError: range() arg 3 must not be zero
>>> names = ["John", "Sally", "Zanthabar"]
>>> names
['John', 'Sally', 'Zanthabar']
>>> names[0]
'John'
>>> type(names[0])
<class 'str'>
>>> names[0].count('o')
1
>>> for name in names:
	print(names.upper())

	
Traceback (most recent call last):
  File "<pyshell#42>", line 2, in <module>
    print(names.upper())
AttributeError: 'list' object has no attribute 'upper'
>>> for name in names:
	print(name.upper())

	
JOHN
SALLY
ZANTHABAR
>>> num = 5
>>> num.upper()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    num.upper()
AttributeError: 'int' object has no attribute 'upper'
>>> nums
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    nums
NameError: name 'nums' is not defined
>>> nums = [1, 2, 3, 4, 5]
>>> nums
[1, 2, 3, 4, 5]
>>> nums.insert(2, 99)
>>> nums
[1, 2, 99, 3, 4, 5]
>>> 