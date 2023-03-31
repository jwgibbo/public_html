Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> random.randint(1, 6)
3
>>> random.randint(1, 6)
5
>>> random.randint(1, 6)
3
>>> random.randint(1, 6)
1
>>> random.randint(1, 6)
3
>>> random.randint(1, 6)
4
>>> random.randint(1, 6)
6
>>> random.randint(1, 6)
4
>>> random.randint(1, 6)
1
>>> random.randint(1, 6)
5
>>> random.randint(1, 6)
6
>>> random.randint(1, 6)
4
>>> random.randint(1, 6)
5
>>> random.randint(1, 6)
6
>>> random.randint(1, 6)
3
>>> random.randint(1, 6)
1
>>> random.randint(1, 6)
6
>>> random.randint(1, 6)
5
>>> random.randint(1, 6)
4
>>> random.randint(1, 6)
5
>>> random.randint(1, 6)
4
>>> random.randint(1, 6)
2
>>> random.randint(1, 20)
9
>>> random.randint(1, 20)
7
>>> dips = ['mayo', 'guac', 'ranch', 'salsa', 'buffalo', 'ketchup', 'bbq']
>>> random.choice(dips)
'salsa'
>>> random.choice(dips)
'ketchup'
>>> random.choice(dips)
'ranch'
>>> random.choice(dips)
'ranch'
>>> random.choice(dips)
'ketchup'
>>> random.choice(dips)
'ketchup'
>>> random.choice(dips)
'ketchup'
>>> random.choice(dips)
'guac'
>>> random.choice(dips)
'guac'
>>> random.choice(dips)
'guac'
>>> random.choice(dips)
'guac'
>>> random.choice(dips)
'salsa'
>>> random.choice(dips)
'bbq'
>>> random.choice(dips)
'buffalo'
>>> random.choice(dips)
'guac'
>>> random.choice(dips)
'mayo'
>>> 
>>> random.choice(dips)
'guac'
>>> random.choice(dips)
'mayo'
>>> 
>>> random.choice(dips)
'mayo'
random.choice(dips)
>>> 
random.choice(dips)
>>> 
random.choice(dips)
>>> 
random.choice(dips)
>>> 
random.choice(dips)
>>> 
random.choice(dips)
>>> 
random.choice(dips)
>>> 
random.choice(dips)
>>> random.choice(dips)
'mayo'
>>> random.choice(dips)
'ranch'
>>> random.choice(dips)
'ketchup'
>>> random.choice(dips)
'ranch'
random.choice(dips)
>>> 
>>> random.choice(dips)
'guac'
>>> random.choice(dips)
'guac'
>>> random.choice(dips)
'mayo'
>>> random.choice(dips)
'guac'
>>> random.choice(dips)
'mayo'
>>> random.choice(dips)
'buffalo'
>>> random.choice(dips)
'guac'
>>> random.choice(dips)
'ketchup'
>>> random.choice(dips)
'bbq'
>>> random.choice(dips)
'guac'
>>> 
>>> random.choice(dips)
'buffalo'
>>> 
>>> p
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    p
NameError: name 'p' is not defined
>>> random.choices(dips, k=3)
['guac', 'salsa', 'bbq']
>>> random.choices(dips, k=3)
['salsa', 'mayo', 'ketchup']
>>> random.choices(dips, k=3)
['ranch', 'buffalo', 'salsa']
>>> random.choices(dips, k=3)
['guac', 'guac', 'ranch']
>>> random.choices(dips, k=3)
['guac', 'guac', 'buffalo']
>>> random.choices(dips, k=3)
['bbq', 'bbq', 'salsa']
>>> random.choices(dips, k=3)
['guac', 'mayo', 'bbq']
>>> random.choices(dips, k=3)
['ketchup', 'bbq', 'mayo']
>>> random.choices(dips, k=3)
['buffalo', 'salsa', 'salsa']
>>> random.choices(dips, k=3)
['mayo', 'bbq', 'ranch']
>>> random.choices(dips, k=3)
['mayo', 'mayo', 'buffalo']
>>> random.choices(dips, k=3)
['bbq', 'bbq', 'guac']
>>> random.choices(dips, k=3)
['salsa', 'salsa', 'ranch']
>>> random.choices(dips, k=3)
['bbq', 'buffalo', 'ranch']
>>> random.choices(dips, k=3)
['mayo', 'bbq', 'ranch']
>>> random.choices(dips, k=3)
['ranch', 'ranch', 'guac']
>>> random.choices(dips, k=30)
['guac', 'salsa', 'salsa', 'ketchup', 'guac', 'ketchup', 'buffalo', 'ketchup', 'buffalo', 'salsa', 'mayo', 'salsa', 'buffalo', 'guac', 'guac', 'buffalo', 'bbq', 'salsa', 'guac', 'bbq', 'ketchup', 'salsa', 'mayo', 'mayo', 'bbq', 'mayo', 'salsa', 'salsa', 'bbq', 'buffalo']
>>> dips
['mayo', 'guac', 'ranch', 'salsa', 'buffalo', 'ketchup', 'bbq']
>>> len(dips)
7
>>> random.sample(dips, k=3)
['bbq', 'ranch', 'buffalo']
>>> random.sample(dips, k=3)
['buffalo', 'ketchup', 'salsa']
>>> random.sample(dips, k=3)
['ketchup', 'guac', 'ranch']
>>> random.sample(dips, k=3)
['bbq', 'salsa', 'guac']
>>> random.sample(dips, k=3)
['ketchup', 'buffalo', 'guac']
>>> random.sample(dips, k=3)
['mayo', 'buffalo', 'salsa']
>>> random.sample(dips, k=3)
['ranch', 'salsa', 'mayo']
>>> random.sample(dips, k=3)
['guac', 'bbq', 'salsa']
>>> random.sample(dips, k=3)
['mayo', 'bbq', 'buffalo']
>>> random.sample(dips, k=3)
['mayo', 'buffalo', 'salsa']
>>> random.sample(dips, k=3)
['ranch', 'mayo', 'guac']
>>> random.sample(dips, k=3)
['buffalo', 'salsa', 'bbq']
>>> random.sample(dips, k=3)
['bbq', 'salsa', 'ketchup']
>>> random.sample(dips, k=3)
['salsa', 'ketchup', 'mayo']
>>> random.sample(dips, k=3)
['ranch', 'bbq', 'guac']
>>> random.sample(dips, k=3)
['salsa', 'buffalo', 'mayo']
>>> random.sample(dips, k=30)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    random.sample(dips, k=30)
  File "C:\Program Files\Python39\lib\random.py", line 449, in sample
    raise ValueError("Sample larger than population or is negative")
ValueError: Sample larger than population or is negative
>>> random.sample(dips)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    random.sample(dips)
TypeError: sample() missing 1 required positional argument: 'k'
>>> random.sample(dips, k=7)
['buffalo', 'mayo', 'ranch', 'ketchup', 'salsa', 'guac', 'bbq']
>>> dips
['mayo', 'guac', 'ranch', 'salsa', 'buffalo', 'ketchup', 'bbq']
>>> random.shuffle(dips)
>>> dips
['mayo', 'ranch', 'bbq', 'salsa', 'buffalo', 'ketchup', 'guac']
>>> random.shuffle(dips)
>>> dips
['ranch', 'salsa', 'guac', 'mayo', 'buffalo', 'ketchup', 'bbq']
>>> dips[0]
'ranch'
>>> 