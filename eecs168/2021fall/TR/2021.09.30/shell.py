Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nums = [5,10,15,20]
>>> nums.append(3)
>>> print(nums.append(55))
None
>>> nums
[5, 10, 15, 20, 3, 55]
>>> len(nums)
6
>>> nums.count(10)
1
>>> nums.index(20)
3
>>> nums.append(20)
>>> nums
[5, 10, 15, 20, 3, 55, 20]
>>> nums.index(20)
3
>>> nums.index(99)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    nums.index(99)
ValueError: 99 is not in list
>>> nums.count(99)
0
>>> 99 in nums
False
>>> nums.index(20)
3
>>> nums.index(20, 4)
6
>>> nums.index(20, 3)
3
>>> nums = [5,10,15,20]
>>> nums
[5, 10, 15, 20]
>>> len(nums)
4
>>> nums.insert(0, -1)
>>> nums
[-1, 5, 10, 15, 20]
>>> nums.insert(5, 99)
>>> nums
[-1, 5, 10, 15, 20, 99]
>>> target_index = nums.index(15)
>>> target_index
3
>>> nums.insert(target_index, 13)
>>> nums
[-1, 5, 10, 13, 15, 20, 99]
>>> nums.insert(1000, 88)
>>> nums
[-1, 5, 10, 13, 15, 20, 99, 88]
>>> nums.insert(-1000, 77)
>>> nums
[77, -1, 5, 10, 13, 15, 20, 99, 88]
>>> nums.index(4)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    nums.index(4)
ValueError: 4 is not in list
>>> nums.(1000000, 4)
SyntaxError: invalid syntax
>>> nums.insert(1000000, 4)
>>> nums
[77, -1, 5, 10, 13, 15, 20, 99, 88, 4]
>>> nums[-1]
4
>>> nums.insert(-1, 5)
>>> nums
[77, -1, 5, 10, 13, 15, 20, 99, 88, 5, 4]
>>> nums.insert(-4, 33)
>>> nums
[77, -1, 5, 10, 13, 15, 20, 33, 99, 88, 5, 4]
>>> nums.insert(len(nums), 222)
>>> nums
[77, -1, 5, 10, 13, 15, 20, 33, 99, 88, 5, 4, 222]
>>> nums = [5, 10, 15, 20]
>>> nums
[5, 10, 15, 20]
>>> nums[-1]
20
>>> nums.insert(2, 77)
>>> nums[2]
77
>>> nums.insert(-1, 99)
>>> nums[-1]
20
>>> nums
[5, 10, 77, 15, 99, 20]
>>> nums.remove(15)
>>> nums
[5, 10, 77, 99, 20]
>>> len(nums)
5
>>> nums.remove(99)
>>> len(nums)
4
>>> nums.pop(1)
10
>>> nums
[5, 77, 20]
>>> nums.pop(1000)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    nums.pop(1000)
IndexError: pop index out of range
>>> nums.pop(-1000)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    nums.pop(-1000)
IndexError: pop index out of range
>>> nums.pop(-1)
20
>>> nums
[5, 77]
>>> 
