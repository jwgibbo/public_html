Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> word = "doggy"
>>> word[0]
'd'
>>> word[4]
'y'
>>> word[6]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    word[6]
IndexError: string index out of range
>>> word[-1]
'y'
>>> word[-5]
'd'
>>> word[-1]
'y'
>>> 
= RESTART: H:/public_html/eecs168/2021fall/MWF/2021.09.13/for-in-loops.py
d
o
g
g
y
>>> range(5)
range(0, 5)
>>> 
= RESTART: H:/public_html/eecs168/2021fall/MWF/2021.09.13/for-in-loops.py
d
o
g
g
y
0
1
2
3
4
>>> 
= RESTART: H:/public_html/eecs168/2021fall/MWF/2021.09.13/for-in-loops.py
d
o
g
g
y
-----
0
1
2
3
4
>>> 
= RESTART: H:/public_html/eecs168/2021fall/MWF/2021.09.13/for-in-loops.py
d
o
g
g
y
-----
0
1
2
3
4
-----
2
4
6
>>> 
= RESTART: H:/public_html/eecs168/2021fall/MWF/2021.09.13/for-in-loops.py
d
o
g
g
y
-----
0
1
2
3
4
-----
2
4
6
8
>>> 
= RESTART: H:/public_html/eecs168/2021fall/MWF/2021.09.13/for-in-loops.py
d
o
g
g
y
-----
0
1
2
3
4
-----
10
9
8
7
6
5
4
3
2
1
>>> 
= RESTART: H:/public_html/eecs168/2021fall/MWF/2021.09.13/for-in-loops.py
d
o
g
g
y
-----
0
1
2
3
4
-----
Traceback (most recent call last):
  File "H:/public_html/eecs168/2021fall/MWF/2021.09.13/for-in-loops.py", line 13, in <module>
    for number in range(2.5,5.0,0.5):
TypeError: 'float' object cannot be interpreted as an integer
>>> 
= RESTART: H:/public_html/eecs168/2021fall/MWF/2021.09.13/for-in-loops.py
d
o
g
g
y
-----
0
1
2
3
4
-----
>>> 
= RESTART: H:/public_html/eecs168/2021fall/MWF/2021.09.13/for-in-loops.py
d
o
g
g
y
-----
0
1
2
3
4
-----
100
99
98
97
96
95
94
93
92
91
90
89
88
87
86
85
84
83
82
81
80
79
78
77
76
75
74
73
72
71
70
69
68
67
66
65
64
63
62
61
60
59
58
57
56
55
54
53
52
51
50
49
48
47
46
45
44
43
42
41
40
39
38
37
36
35
34
33
32
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
15
14
13
12
11
>>> 