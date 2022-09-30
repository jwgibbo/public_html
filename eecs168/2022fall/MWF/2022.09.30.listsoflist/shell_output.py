Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> demo_line = 'PRINT'
>>> demo_line.split(' ')
['PRINT']
>>> 'ADD' in 'ADD duck'
True
>>> line = 'ADD duck'
>>> 'ADD' in line
True
>>> line[4:]
'duck'
>>> my_list = [5, 'cat', True]
>>> my_list
[5, 'cat', True]
>>> type(my_list[1])
<class 'str'>
>>> my_list[1].upper()
'CAT'
>>> my_list[2] = 99
>>> my_list
[5, 'cat', 99]
>>> grid = []
>>> grid.append( [10, 20, 30] )
>>> grid.append( [40, 50, 60] )
>>> len(grid)
2
>>> word = 'cats'
>>> len(word)
4
>>> grid
[[10, 20, 30], [40, 50, 60]]
>>> type(grid)
<class 'list'>
>>> type(grid[0])
<class 'list'>
>>> grid[0][2]
30
>>> groceries = [ ['apples'] ]
>>> 