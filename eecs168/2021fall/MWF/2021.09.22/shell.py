Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 55
>>> num
55
>>> word = "candy"
>>> word
'candy'
>>> word[3]
'd'
>>> word[1:4]
'and'
>>> nums = [2,3,5,8]
>>> nums
[2, 3, 5, 8]
>>> type(nums)
<class 'list'>
>>> nums
[2, 3, 5, 8]
>>> 5 in nums
True
>>> nums[3]
8
>>> nums[3] = 7
>>> nums
[2, 3, 5, 7]
>>> word
'candy'
>>> word[0] = 'd'
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    word[0] = 'd'
TypeError: 'str' object does not support item assignment
>>> type(word)
<class 'str'>
>>> type(word[0])
<class 'str'>
>>> type('d')
<class 'str'>
>>> type('dddddddddddddddddddd')
<class 'str'>
>>> word = 'dandy'
>>> word = 'c' + word[1:len(word)]
>>> word
'candy'
>>> word = 'c' + word[1:]
>>> word
'candy'
>>> word
'candy'
>>> word = "cannedgood"
>>> word = "candy"
>>> word[0:3]
'can'
>>> word = word[0:3] + "nedgood"
>>> word
'cannedgood'
>>> word[0:]
'cannedgood'
>>> word = 'bat'
>>> word
'bat'
>>> word[0:]
'bat'
>>> word[0::2]
'bt'
>>> word = "batwoman"
>>> word[0::2]
'btoa'
>>> word[0::100]
'b'
>>> word[5::-1]
'mowtab'
>>> word[:]
'batwoman'
>>> word[::-1]
'namowtab'
>>> word[-1:len(word)+1:-1]
''
>>> word[-1:-(len(word)+1):-1]
'namowtab'
>>> nums
[2, 3, 5, 7]
>>> nums[::-1]
[7, 5, 3, 2]
>>> nums.reverse()
>>> nums
[7, 5, 3, 2]
>>> nums
[7, 5, 3, 2]
>>> nums.reverse()
>>> nums
[2, 3, 5, 7]
>>> nums[::-1]
[7, 5, 3, 2]
>>> nums
[2, 3, 5, 7]
>>> word = "taco"
>>> word[::-1]
'ocat'
>>> word
'taco'
>>> word
'taco'
>>> word = word[::-1]
>>> word
'ocat'
>>> string_as_list = list(word)
>>> string_as_list
['o', 'c', 'a', 't']
>>> string_as_list.reverse()
>>> string_as_list
['t', 'a', 'c', 'o']
>>> string_as_list.reverse()
>>> string_as_list
['o', 'c', 'a', 't']
>>> 