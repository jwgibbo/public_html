Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("hello")
hello
>>> print(55)
55
>>> 8**100
2037035976334486086268445688409378161051468393665936250636140449354381299763336706183397376
>>> x = 5
>>> x
5
>>> x+2
7
>>> x = 3+2*4-1
>>> x
10
>>> x
10
>>> type(x)
<class 'int'>
>>> x = 3.5
>>> type(x)
<class 'float'>
>>> x = "hello"
>>> type(x)
<class 'str'>
>>> type(2.0)
<class 'float'>
>>> type(2)
<class 'int'>
>>> x = 3.5
>>> y = 7
>>> x + y
10.5
>>> type(x+y)
<class 'float'>
>>> type(x)
<class 'float'>
>>> type(y)
<class 'int'>
>>> type(2+2)
<class 'int'>
>>> type(2+2.0)
<class 'float'>
>>> 3/2
1.5
>>> 2+2
4
>>> word = hello
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    word = hello
NameError: name 'hello' is not defined
>>> word = "hello"
>>> word
'hello'
>>> word = 'hello'
>>> word = "abc"
>>> word = "ab"
>>> word = "a"
>>> word = ""
>>> word = str(5)
>>> word
'5'
>>> "abc5"
'abc5'
>>> "abc"+"def"
'abcdef'
>>> x = 3+2
>>> x
5
>>> x = 3 + '2'
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    x = 3 + '2'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> x = 3 + int('2')
>>> x
5
>>> word = "12345"
>>> int(word)
12345
>>> type(word)
<class 'str'>
>>> int(word)
12345
>>> word
'12345'
>>> word = int(word)
>>> word
12345
>>> type(word)
<class 'int'>
>>> round(3.4)
3
>>> round(3.5)
4
>>> 3/2
1.5
>>> int(3/2)
1
>>> 3/2
1.5
>>> 3//2
1
>>> 7/5
1.4
>>> 7//5
1
>>> 7%5
2
>>> 11%5
1
>>> 6%2
0
>>> 11%10
1
>>> 12%10
2
>>> 13%10
3
>>> 5578%10
8
>>> 123456789%10
9
>>> 10%2
0
>>> 9%2
1
>>> 8%2
0
>>> 7%2
1
>>> 6%2
0
>>> 35757757675%2
1
>>> 3%5
3
>>> word = "hello"
>>> words = "Hello!"
>>> words
'Hello!'
>>> word
'hello'
>>> num = 5
>>> Num = 6
>>> NUM = 7
>>> num
5
>>> Num
6
>>> NUM
7
>>> age = input("Enter your age: ")
Enter your age: 37
>>> age
'37'
>>> type(age)
<class 'str'>
>>> age + 10
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    age + 10
TypeError: can only concatenate str (not "int") to str
>>> int(age) + 10
47
>>> type(age)
<class 'str'>
>>> age = int( input("Enter your age: ") )
Enter your age: 37
>>> age
37
>>> type(int)
<class 'type'>
>>> type(age)
<class 'int'>
>>> name = input("Enter your name")
Enter your nameabc
>>> name = input("Enter your name: ")
Enter your name: John William Gibbons
>>> name
'John William Gibbons'
>>> age = int(input("Enter your age: "))
Enter your age: 3 7
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    age = int(input("Enter your age: "))
ValueError: invalid literal for int() with base 10: '3 7'
>>> int("3 7")
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    int("3 7")
ValueError: invalid literal for int() with base 10: '3 7'
>>> int("3737337393858")
3737337393858
>>> 