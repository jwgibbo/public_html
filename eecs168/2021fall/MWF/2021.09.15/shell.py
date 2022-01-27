Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: H:/public_html/eecs168/2021fall/MWF/2021.09.15/for-in.py
doggy
doggy
doggy
doggy
doggy
>>> 
= RESTART: H:/public_html/eecs168/2021fall/MWF/2021.09.15/for-in.py
d
o
g
g
y
>>> 
= RESTART: H:/public_html/eecs168/2021fall/MWF/2021.09.15/for-in.py
d
o
g
g
y
word = doggy
>>> name = "Rumpelstelskein"
>>> len(name)
15
>>> 
= RESTART: H:/public_html/eecs168/2021fall/MWF/2021.09.15/for-in.py
d
o
g
g
y
d
o
g
g
y
>>> 
= RESTART: H:/public_html/eecs168/2021fall/MWF/2021.09.15/for-in.py
d
o
g
g
y
-----
d
o
g
g
y
>>> 
= RESTART: H:/public_html/eecs168/2021fall/MWF/2021.09.15/for-in.py
d
o
g
g
y
-----
d
o
g
g
y
Traceback (most recent call last):
  File "H:/public_html/eecs168/2021fall/MWF/2021.09.15/for-in.py", line 16, in <module>
    for digit in 12345:
TypeError: 'int' object is not iterable
>>> pirate_scream = "RRRRRrrrrrRRRrrRRRr!"
>>> type(pirate_scream)
<class 'str'>
>>> len(pirate_scream)
20
>>> pirate_scream.count("R")
11
>>> pirate_scream.count("r")
8
>>> len(pirate_scream)
20
>>> pirate_scream.count("!")
1
>>> pirate_scream.count("C")
0
>>> pirate_scream.count("RRR")
3
>>> len(pirate_scream)
20
>>> pirate_scream.count("RRRRR")
1
>>> 