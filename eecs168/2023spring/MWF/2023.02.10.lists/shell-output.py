Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> word = 'friday'
>>> word[::]
'friday'
>>> word[::1]
'friday'
>>> nums = []
>>> nums
[]
>>> type(nums)
<class 'list'>
>>> len(nums)
0
>>> letters = list('demagogue')
>>> letters
['d', 'e', 'm', 'a', 'g', 'o', 'g', 'u', 'e']
>>> len(letters)
9
>>> nums
[]
>>> nums = [5, 10, 15, 20]
>>> nums
[5, 10, 15, 20]
>>> nums[2]
15
>>> nums
[5, 10, 15, 20]
>>> for num in nums:
	print(num)

	
5
10
15
20
>>> nums
[5, 10, 15, 20]
>>> nums[2] = 99
>>> nums
[5, 10, 99, 20]
>>> nums[1:4:2]
[10, 20]
>>> nums
[5, 10, 99, 20]
>>> nums.append(55)
>>> nums
[5, 10, 99, 20, 55]
>>> nums.insert(3, 21)
>>> nums
[5, 10, 99, 21, 20, 55]
>>> nums.pop(4)
20
>>> nums
[5, 10, 99, 21, 55]
>>> 