Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> word = "dog"
>>> word[1]
'o'
>>> word[1] = 'i'
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    word[1] = 'i'
TypeError: 'str' object does not support item assignment
>>> word = word + i
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    word = word + i
NameError: name 'i' is not defined
>>> word = word + 'i'
>>> word
'dogi'
>>> nums = [5, 7, 13, 23]
>>> nums
[5, 7, 13, 23]
>>> x = int(2.5)
>>> x
2
>>> letters = list("doggy")
>>> letters
['d', 'o', 'g', 'g', 'y']
>>> nums[0]
5
>>> nums[-1]
23
>>> len(nums)
4
>>> nums[0:3]
[5, 7, 13]
>>> nums[2] = 7
>>> nums
[5, 7, 7, 23]
>>> nums.append(49)
>>> nums
[5, 7, 7, 23, 49]
>>> nums.append(55)
>>> nums
[5, 7, 7, 23, 49, 55]
>>> nums.append(2)
>>> nums
[5, 7, 7, 23, 49, 55, 2]
>>> letters
['d', 'o', 'g', 'g', 'y']
>>> str_from_list = str(letters)
>>> str_from_list
"['d', 'o', 'g', 'g', 'y']"
>>> len(str_from_list)
25
>>> nums
[5, 7, 7, 23, 49, 55, 2]
>>> 55 in nums
True
>>> nums.count(55)
1
>>> nums = nums + 99
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    nums = nums + 99
TypeError: can only concatenate list (not "int") to list
>>> 