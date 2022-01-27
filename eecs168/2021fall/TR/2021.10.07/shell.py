Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: H:/public_html/eecs168/2021fall/TR/2021.10.07/function-scope.py
55
>>> 
= RESTART: H:/public_html/eecs168/2021fall/TR/2021.10.07/function-scope.py
55
Traceback (most recent call last):
  File "H:/public_html/eecs168/2021fall/TR/2021.10.07/function-scope.py", line 7, in <module>
    print(ans)
NameError: name 'ans' is not defined
>>> 
= RESTART: H:/public_html/eecs168/2021fall/TR/2021.10.07/function-scope.py
>>> 
 = RESTART: H:/public_html/eecs168/2021fall/TR/2021.10.07/function-scope.py
55
Traceback (most recent call last):
  File "H:/public_html/eecs168/2021fall/TR/2021.10.07/function-scope.py", line 14, in <module>
    main()
  File "H:/public_html/eecs168/2021fall/TR/2021.10.07/function-scope.py", line 8, in main
    print(ans)
NameError: name 'ans' is not defined
>>> 
= RESTART: H:/public_html/eecs168/2021fall/TR/2021.10.07/function-scope.py
55
>>> 
= RESTART: H:/public_html/eecs168/2021fall/TR/2021.10.07/function-scope.py
Program started
55
Program exiting...
>>> 
= RESTART: H:/public_html/eecs168/2021fall/TR/2021.10.07/function-scope.py
Program started
Enter a number: 54
Here is your number plus one!: 55
Program exiting...
>>> "abc","def"
('abc', 'def')
>>> type("abc","def")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    type("abc","def")
TypeError: type() takes 1 or 3 arguments
>>> type(("abc","def"))
<class 'tuple'>
>>> float("4.5")
4.5
>>> list("banana")
['b', 'a', 'n', 'a', 'n', 'a']
>>> len("banana")
6
>>> len( list("banana") )
6
>>> banana_list = list("banana")
>>> str(banana_list)
"['b', 'a', 'n', 'a', 'n', 'a']"
>>> len(str(banana_list))
30
>>> delimiter = ","
>>> fruits = ["strawberry", "corn", "pumpkin"]
>>> fruits
['strawberry', 'corn', 'pumpkin']
>>> delimiter.join(fruits)
'strawberry,corn,pumpkin'
>>> type(delimiter.join(fruits))
<class 'str'>
>>> fruit_string = "apple,orange,mango"
>>> fruit_string
'apple,orange,mango'
>>> fruit_string.split(delimiter)
['apple', 'orange', 'mango']
>>> fruits
['strawberry', 'corn', 'pumpkin']
>>> str(fruits)
"['strawberry', 'corn', 'pumpkin']"
>>> word = "cat"
>>> word
'cat'
>>> word[0] = 'b'
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    word[0] = 'b'
TypeError: 'str' object does not support item assignment
>>> letters = ['c','a','t']
>>> letters
['c', 'a', 't']
>>> letter[0] = 'b'
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    letter[0] = 'b'
NameError: name 'letter' is not defined
>>> letters[0] = 'b'
>>> letters
['b', 'a', 't']
>>> letters.reverse()
>>> letters
['t', 'a', 'b']
>>> word
'cat'
>>> word.reverse()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    word.reverse()
AttributeError: 'str' object has no attribute 'reverse'
>>> letters.reverse()
>>> letters
['b', 'a', 't']
>>> letters.reverse()
>>> letters
['t', 'a', 'b']
>>> letters[::-1]
['b', 'a', 't']
>>> letters
['t', 'a', 'b']
>>> word
'cat'
>>> word[::-1]
'tac'
>>> word
'cat'
>>> 
= RESTART: H:/public_html/eecs168/2021fall/TR/2021.10.07/function-scope.py
Program started
almond joy
twix
snickers
whoppers
Program exiting...
>>> 
= RESTART: H:/public_html/eecs168/2021fall/TR/2021.10.07/function-scope.py
Program started
10
4
8
8
Program exiting...
>>> 
= RESTART: H:/public_html/eecs168/2021fall/TR/2021.10.07/function-scope.py
Program started
alm
twi
sni
who
Program exiting...
>>> 
= RESTART: H:/public_html/eecs168/2021fall/TR/2021.10.07/function-scope.py
Program started
a
l
m
o
n
d
 
j
o
y
-----
t
w
i
x
-----
s
n
i
c
k
e
r
s
-----
w
h
o
p
p
e
r
s
-----
Program exiting...
>>> 
= RESTART: H:/public_html/eecs168/2021fall/TR/2021.10.07/function-scope.py
Program started
a
-----
l
-----
m
-----
o
-----
n
-----
d
-----
 
-----
j
-----
o
-----
y
-----
t
-----
w
-----
i
-----
x
-----
s
-----
n
-----
i
-----
c
-----
k
-----
e
-----
r
-----
s
-----
w
-----
h
-----
o
-----
p
-----
p
-----
e
-----
r
-----
s
-----
Program exiting...
>>> 
= RESTART: H:/public_html/eecs168/2021fall/TR/2021.10.07/function-scope.py
Program started
a
l
m
o
n
d
 
j
o
y
t
w
i
x
s
n
i
c
k
e
r
s
w
h
o
p
p
e
r
s
-----
Program exiting...
>>> 
= RESTART: H:/public_html/eecs168/2021fall/TR/2021.10.07/function-scope.py
Program started
a
l
m
o
n
d
 
j
o
y
-----
t
w
i
x
-----
s
n
i
c
k
e
r
s
-----
w
h
o
p
p
e
r
s
-----
Program exiting...
>>> input("enter a guess: ")
enter a guess: banana
'banana'
>>> user_guess = input("Enter a guess: ")
Enter a guess: banana
>>> user_guess
'banana'
>>> 