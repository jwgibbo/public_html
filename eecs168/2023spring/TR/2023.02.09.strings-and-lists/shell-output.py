Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
word = 'career'
word[2]
'r'
word[0]
'c'
word[99]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    word[99]
IndexError: string index out of range
len(word)
6
word[5]
'r'
word[len(word)-1]
'r'
word[len(word)]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    word[len(word)]
IndexError: string index out of range
word = 'bat'
word
'bat'
word[0]
'b'
word[0] = 'c'
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    word[0] = 'c'
TypeError: 'str' object does not support item assignment
letters = 'abcdefgh'
len(letters)
8
letters[1:6]
'bcdef'
letters[0:6:2]
'ace'
letters[0:7:2]
'aceg'
letters[0:len(letters):2]
'aceg'
letters[1:99]
'bcdefgh'
letters[99]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    letters[99]
IndexError: string index out of range
letters
'abcdefgh'
letters[-1]
'h'
letters[-8]
'a'
letters[-len(letters)]
'a'
letters[0]
'a'
letters[-1:-5:-1]
'hgfe'
letters[-1: -(len(letters)+1) : -1]
'hgfedcba'
letters[::-1]
'hgfedcba'
nums = []
nums
[]
len(nums)
0
nums = [5, 10, 15]
nums
[5, 10, 15]
len(nums)
3
nums[2]
15
for num in nums:
    print(num)

    
5
10
15
nums[1] = 25
nums
[5, 25, 15]
nums[::-1]
[15, 25, 5]
nums
[5, 25, 15]
nums
[5, 25, 15]
nums.append(45)
nums
[5, 25, 15, 45]
len(nums)
4
nums.append(55)
nums
[5, 25, 15, 45, 55]
nums[2]
15
nums.insert(2, 99)
nums
[5, 25, 99, 15, 45, 55]
nums[2]
99
nums[3]
15
nums.pop(4)
45
nums
[5, 25, 99, 15, 55]

= RESTART: C:/Users/jwgib/OneDrive/Desktop/public_html/eecs168/2023spring/TR/2023.02.09.strings-and-lists/listdemo.py
Enter a number: 5
Enter a number: 10
Enter a number: 
Traceback (most recent call last):
  File "C:/Users/jwgib/OneDrive/Desktop/public_html/eecs168/2023spring/TR/2023.02.09.strings-and-lists/listdemo.py", line 5, in <module>
    num3 = int(input("Enter a number: "))
ValueError: invalid literal for int() with base 10: ''

= RESTART: C:/Users/jwgib/OneDrive/Desktop/public_html/eecs168/2023spring/TR/2023.02.09.strings-and-lists/listdemo.py
Enter a number: 5
Enter a number: 10
Enter a number: 15
Enter a number: 20
Enter a number: 25
=======
Enter a number: 5
Enter a number: 10
Enter a number: 15
Enter a number: 50
Enter a number: 75
>>> 
= RESTART: C:/Users/jwgib/OneDrive/Desktop/public_html/eecs168/2023spring/TR/2023.02.09.strings-and-lists/listdemo.py
Enter a number: 1
Enter a number: 2
Enter a number: 3
Enter a number: 4
Enter a number: 5
=======
Enter a number: 5
Enter a number: 10
Enter a number: 15
Enter a number: 20
Enter a number: 25
[5, 10, 15, 20, 25]
