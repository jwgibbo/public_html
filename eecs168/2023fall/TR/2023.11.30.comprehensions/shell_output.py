Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nums = [5, 10, 15, 20, 25, 30]
>>> odds = [num for num in nums if num%2==1]
>>> odds
[5, 15, 25]
>>> odd_cubes = [num**3 for num in nums if num%2==1]
>>> num_days = 6
>>> 'ahhhhh' if num_day < 10 else 'phew'
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    'ahhhhh' if num_day < 10 else 'phew'
NameError: name 'num_day' is not defined
>>> 'ahhhhh' if num_days < 10 else 'phew'
'ahhhhh'
>>> num_days = 40
>>> 'ahhhhh' if num_days < 10 else 'phew'
'phew'
>>> nums
[5, 10, 15, 20, 25, 30]
>>> [num**2 if num%2==0 else num**3 for num in nums]
[125, 100, 3375, 400, 15625, 900]
>>> new_list = [num**2 if num%2==0 else num**3 for num in nums]
>>> new_list
[125, 100, 3375, 400, 15625, 900]
>>> nums
[5, 10, 15, 20, 25, 30]
>>> new_list = [num**2 if num%2==0 else num**3 for num in nums if num > 17]
>>> new_list
[400, 15625, 900]
>>> 