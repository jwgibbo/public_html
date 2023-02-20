Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = int('3287')
>>> nums
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    nums
NameError: name 'nums' is not defined
>>> num
3287
>>> groceries = 'oranges,apples,nuts'

>>> grocery_list = list(groceries)
>>> grocery_list
['o', 'r', 'a', 'n', 'g', 'e', 's', ',', 'a', 'p', 'p', 'l', 'e', 's', ',', 'n', 'u', 't', 's']
>>> nums = [13, 55, 42, 8, 1]
>>> nums_string = str(nums)
>>> len(nums)
5
>>> len(nums_string)
18
>>> nums_string
'[13, 55, 42, 8, 1]'
>>> groceries = 'oranges,apples,nuts'
>>> grocery_list = groceries.split(',')
>>> grocery_list
['oranges', 'apples', 'nuts']
>>> len(grocery_list)
3
>>> for item in grocery_list:
	print(item)

	
oranges
apples
nuts
>>> grocery_list
['oranges', 'apples', 'nuts']
>>> str(grocery_list)
"['oranges', 'apples', 'nuts']"
>>> grocery_list
['oranges', 'apples', 'nuts']
>>> delimiter = ','
>>> delimiter.join(grocery_list)
'oranges,apples,nuts'
>>> delimiter = 'ICING'
>>> delimiter.join(grocery_list)
'orangesICINGapplesICINGnuts'
>>> 