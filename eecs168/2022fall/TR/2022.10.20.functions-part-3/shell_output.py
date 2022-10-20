Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 342
>>> num[0]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    num[0]
TypeError: 'int' object is not subscriptable
>>> num[::-1]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    num[::-1]
TypeError: 'int' object is not subscriptable
>>> num.append(8)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    num.append(8)
AttributeError: 'int' object has no attribute 'append'
>>> nums1 = [5, 10, 15, 20]
>>> nums2 = nums1
>>> nums1
[5, 10, 15, 20]
>>> nums2
[5, 10, 15, 20]
>>> nums2[0] = 99
>>> nums1
[99, 10, 15, 20]
>>> nums2
[99, 10, 15, 20]
>>> nums1
[99, 10, 15, 20]
>>> for num in nums1:
	num = 0

	
>>> nums1
[99, 10, 15, 20]
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

>>> grades = {}
>>> type(grades)
<class 'dict'>
>>> grades['john'] = 55
>>> grades['luna'] = 98
>>> grades['alec'] = 98
>>> grades
{'john': 55, 'luna': 98, 'alec': 98}
>>> len(grades)
3
>>> grades['john']
55
>>> for student, grade in grades:
	print(f'{student} got a(n) {grade}')

	
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    for student, grade in grades:
ValueError: too many values to unpack (expected 2)
>>> for student, grade in grades.items():
	print(f'{student} got a(n) {grade}')

	
john got a(n) 55
luna got a(n) 98
alec got a(n) 98
>>> 