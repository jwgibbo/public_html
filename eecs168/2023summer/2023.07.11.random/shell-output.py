Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> random.randint(1, 6)
6
>>> random.randint(1, 6)
6
>>> random.randint(1, 6)
5
>>> random.randint(1, 6)
1
>>> random.randint(1, 6)
5
>>> random.randint(1, 6)
4
>>> random.randint(1, 6)
6
>>> random.randint(1, 6)
6
>>> random.randint(1, 6)
6
>>> random.randint(1, 6)
3
>>> random.randint(1, 6)
1
>>> random.randint(1, 6)
4
>>> random.randint(1, 6)
6
random.randint(1, 6)
3
random.randint(1, 6)
4
random.randint(1, 6)
2
random.randint(1, 20)
9
random.randint(1, 20)
7
random.randint(1, 20)
12
students = ['braxton', 'ethan', 'ibrahim', 'keaton', 'kieran', 'oris', 'viren']
random.choice(student)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    random.choice(student)
NameError: name 'student' is not defined. Did you mean: 'students'?
random.choice(students)
'ethan'
random.choices(students, k=3)
['oris', 'viren', 'keaton']
random.choices(students, k=3)
['braxton', 'keaton', 'oris']
random.choices(students, k=3)
['kieran', 'braxton', 'viren']
random.choices(students, k=3)
['oris', 'kieran', 'keaton']
random.choices(students, k=3)
['braxton', 'keaton', 'ethan']
random.choices(students, k=3)
['keaton', 'ethan', 'viren']
random.choices(students, k=3)
['oris', 'oris', 'braxton']
len(students)
7
random.choices(students, k=25)
['ibrahim', 'ethan', 'kieran', 'viren', 'viren', 'ibrahim', 'kieran', 'oris', 'braxton', 'keaton', 'keaton', 'ethan', 'ethan', 'keaton', 'keaton', 'kieran', 'ethan', 'ethan', 'keaton', 'oris', 'keaton', 'viren', 'ibrahim', 'ibrahim', 'ethan']
len(students)
7
students
['braxton', 'ethan', 'ibrahim', 'keaton', 'kieran', 'oris', 'viren']
random.sample(students, 4)
['keaton', 'oris', 'ethan', 'kieran']
random.sample(students, 4)
['braxton', 'viren', 'ethan', 'oris']
random.sample(students, 4)
['keaton', 'braxton', 'oris', 'ethan']
random.sample(students, 4)
['oris', 'kieran', 'ibrahim', 'keaton']
random.sample(students, 4)
['kieran', 'keaton', 'ibrahim', 'ethan']
random.sample(students, 4)
['oris', 'ethan', 'keaton', 'kieran']
random.sample(students, 4)
['ethan', 'ibrahim', 'kieran', 'keaton']
random.sample(students, 4)
['viren', 'kieran', 'keaton', 'ethan']
random.sample(students, 4)
['kieran', 'ibrahim', 'keaton', 'viren']
random.sample(students, 4)
['keaton', 'kieran', 'oris', 'viren']
random.sample(students, 7)
['braxton', 'ibrahim', 'kieran', 'oris', 'viren', 'keaton', 'ethan']
random.sample(students, 8)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    random.sample(students, 8)
  File "C:\Users\jwgib\AppData\Local\Programs\Python\Python311\Lib\random.py", line 453, in sample
    raise ValueError("Sample larger than population or is negative")
ValueError: Sample larger than population or is negative
students
['braxton', 'ethan', 'ibrahim', 'keaton', 'kieran', 'oris', 'viren']
random.shuffle(students)
students
['ethan', 'braxton', 'ibrahim', 'keaton', 'viren', 'oris', 'kieran']
x = range(1,5)
x[0]
1
random.sample(range(1, 70),k=6)

[37, 44, 29, 4, 28, 2]
