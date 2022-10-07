Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> float('rootbeer')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    float('rootbeer')
ValueError: could not convert string to float: 'rootbeer'
>>> word = 'catFOOD'
>>> word.upper()
'CATFOOD'
>>> 'A'*1000
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
>>> 
>>> 

>>> 
>>> 
>>> 

>>> 
>>> 
>>> 

>>> 
>>> 

>>> 
>>> 
>>> 
>>> 

>>> 
>>> 
>>> 
>>> 
>>> not True
False
>>> not False
True
>>> not 3<5
False
>>> for num in range(1, 11):
	print(num)

	
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
>>> for num in range(5):
	print(num)

	
0
1
2
3
4
>>> for num in range(2, 9, 2):
	print(num)

	
2
4
6
8
>>> for num in range(2, 9, -2):
	print(num)

	
>>> for num in range(2, -9, -2):
	print(num)

	
2
0
-2
-4
-6
-8
>>> candies = ['skittles', 'twix', 'reeces']
>>> 
>>> candies
['skittles', 'twix', 'reeces']
>>> delmiter = '!'
>>> delimiter = '!'
>>> delimiter.join(candies)
'skittles!twix!reeces'
>>> delimiter
'!'
>>> candies
['skittles', 'twix', 'reeces']
>>> movies = 'Halloween,Cujo,Dracula'
>>> movies
'Halloween,Cujo,Dracula'
>>> list(movies)
['H', 'a', 'l', 'l', 'o', 'w', 'e', 'e', 'n', ',', 'C', 'u', 'j', 'o', ',', 'D', 'r', 'a', 'c', 'u', 'l', 'a']
>>> movies.split(',')
['Halloween', 'Cujo', 'Dracula']
>>> my_string = '   A B C       '
>>> len(my_string)
15
>>> my_string.strip()
'A B C'
>>> movies
'Halloween,Cujo,Dracula'
>>> movies.count('l')
3
>>> movies.count('ll')
1
>>> movies.find('l')
2
>>> movies.find('z')
-1
>>> 