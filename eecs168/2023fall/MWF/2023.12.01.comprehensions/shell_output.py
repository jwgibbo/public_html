Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> original = [5, 10, 15, 20, 25, 30]
>>> original
[5, 10, 15, 20, 25, 30]
>>> squares = [num**2 for num in original]
>>> squares
[25, 100, 225, 400, 625, 900]
>>> nums
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    nums
NameError: name 'nums' is not defined
>>> original
[5, 10, 15, 20, 25, 30]
>>> odds = [num for num in original if num%2==1]
>>> odds
[5, 15, 25]
>>> days_left = 5
>>> 'Ut oh' if days_left < 20 else 'phew'
'Ut oh'
>>> 