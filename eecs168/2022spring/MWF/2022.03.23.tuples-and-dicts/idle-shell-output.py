Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_tup = (5, 10, 15, 20)
>>> my_tup
(5, 10, 15, 20)
>>> type(my_tup)
<class 'tuple'>
>>> my_tup[0]
5
>>> for num in my_tup:
	print(num)

	
5
10
15
20
>>> my_tup[0] = 99
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    my_tup[0] = 99
TypeError: 'tuple' object does not support item assignment
>>> my_confusing_tup = ([1,2,3], [4,5,6])
>>> my_confusing_tup
([1, 2, 3], [4, 5, 6])
>>> my_confusing_tup[0] = 5
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    my_confusing_tup[0] = 5
TypeError: 'tuple' object does not support item assignment
>>> my_confusing_tup[0]
[1, 2, 3]
>>> x = 5
>>> y = 10
>>> z = 15
>>> my_tup = (x, y, z)
>>> my_tup
(5, 10, 15)
>>> x = 99
>>> my_tup
(5, 10, 15)
>>> x = 5
>>> y = x
>>> x = 99
>>> x
99
>>> y
5
>>> my_tup.count(5)
1
>>> my_tup.index(5)
0
>>> list_of_grades = [99, 67, 85, 74]
>>> list_of_grades
[99, 67, 85, 74]
>>> grades = {}
>>> type(grades)
<class 'dict'>
>>> grade['john'] = 55
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    grade['john'] = 55
NameError: name 'grade' is not defined
>>> grades['john'] = 55
>>> grades['mary'] = 98
>>> grades['chimichumi'] = 88
>>> grades
{'john': 55, 'mary': 98, 'chimichumi': 88}
>>> len(grades)
3
>>> grades['mary']
98
>>> print(grades)
{'john': 55, 'mary': 98, 'chimichumi': 88}
>>> for student, grade in grades.items():
	print(student + " got a " + str(grade))

	
john got a 55
mary got a 98
chimichumi got a 88
>>> for item in grades:
	print(item)

	
john
mary
chimichumi
>>> 