Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nums = [5, 10, 55, 3]
>>> nums
[5, 10, 55, 3]
>>> nums.index(55)
2
>>> nums.append(55)
>>> nums
[5, 10, 55, 3, 55]
>>> nums.index(55)
2
>>> nums.index(99)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    nums.index(99)
ValueError: 99 is not in list
>>> nums.count(99)
0
>>> 99 in nums
False
>>> len(nums)
5
>>> nums.insert(7, 99)
>>> nums
[5, 10, 55, 3, 55, 99]
>>> nums.insert(100, -1)
>>> nums
[5, 10, 55, 3, 55, 99, -1]
>>> nums.index(2)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    nums.index(2)
ValueError: 2 is not in list
>>> nums.index(-1)
6
>>> nums.insert(-100, 42)
>>> nums
[42, 5, 10, 55, 3, 55, 99, -1]
>>> nums.insert(3, 87)
>>> nums
[42, 5, 10, 87, 55, 3, 55, 99, -1]
>>> nums.insert(nums.index(55), 0)
>>> nums
[42, 5, 10, 87, 0, 55, 3, 55, 99, -1]
>>> nums.remove(55)
>>> nums
[42, 5, 10, 87, 0, 3, 55, 99, -1]
>>> nums.remove(55)
>>> nums
[42, 5, 10, 87, 0, 3, 99, -1]
>>> nums.remove(55)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    nums.remove(55)
ValueError: list.remove(x): x not in list
>>> nums
[42, 5, 10, 87, 0, 3, 99, -1]
>>> nums.pop(0)
42
>>> nums
[5, 10, 87, 0, 3, 99, -1]
>>> quick_list = ['']
>>> quick_list
['']
>>> len(quick_list)
1
>>> quick_list = ['']*3
>>> quick_list
['', '', '']
>>> len(quick_list)
3
>>> 