Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Users/jwgib/OneDrive/Desktop/public_html/eecs168/2023spring/TR/2023.02.16.lists-and-string/indemo.py
Enter a number: 55
No it is not in the list
No it is not in the list
No it is not in the list
No it is not in the list
Yes it is in the list
No it is not in the list
No it is not in the list

= RESTART: C:/Users/jwgib/OneDrive/Desktop/public_html/eecs168/2023spring/TR/2023.02.16.lists-and-string/indemo.py
Enter a number: 55
Yes it is in the list

= RESTART: C:/Users/jwgib/OneDrive/Desktop/public_html/eecs168/2023spring/TR/2023.02.16.lists-and-string/indemo.py
Enter a number: 55
Yes it is in the list
Yes it is in the list
Yes it is in the list

= RESTART: C:/Users/jwgib/OneDrive/Desktop/public_html/eecs168/2023spring/TR/2023.02.16.lists-and-string/indemo.py
Enter a number: 55
Your number is in the list

= RESTART: C:/Users/jwgib/OneDrive/Desktop/public_html/eecs168/2023spring/TR/2023.02.16.lists-and-string/indemo.py
Enter a number: 55
Your number is in the list

= RESTART: C:/Users/jwgib/OneDrive/Desktop/public_html/eecs168/2023spring/TR/2023.02.16.lists-and-string/indemo.py
Enter a number: 55
Your number is NOT in the list

= RESTART: C:/Users/jwgib/OneDrive/Desktop/public_html/eecs168/2023spring/TR/2023.02.16.lists-and-string/indemo.py
Enter a number: 7
Your number is in the list
Your number is in the list

= RESTART: C:/Users/jwgib/OneDrive/Desktop/public_html/eecs168/2023spring/TR/2023.02.16.lists-and-string/indemo.py
Enter a number: 99
Your number is NOT in the list
Your number is NOT in the list
word = 'dangerous'
len(word)
9
word_as_list = list(word)
word_as
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    word_as
NameError: name 'word_as' is not defined
word_as_list
['d', 'a', 'n', 'g', 'e', 'r', 'o', 'u', 's']
groceries_str = 'oranges,apples,oats,nuts'
groceries_list = list(groceries_str)
len(groceries_list)
24
groceries_list
['o', 'r', 'a', 'n', 'g', 'e', 's', ',', 'a', 'p', 'p', 'l', 'e', 's', ',', 'o', 'a', 't', 's', ',', 'n', 'u', 't', 's']
 groceries_list = groceries_str.split(',')
 
SyntaxError: unexpected indent
groceries_list = groceries_str.split(',')
groceries_list
['oranges', 'apples', 'oats', 'nuts']
letter = ['a','b','c']
letters = ['a','b','c']
len(letters)
3
letters_as_string = str(letters)
len(letters_as_string)
15
letters_as_string
"['a', 'b', 'c']"
delimiter = '?'
letters_as_string = delimiter.join(letters)
>>> letters_as_string
'a?b?c'
>>> delimiter = '' #empty string
>>> letters_as_string = delimiter.join(letters)
>>> letters_as_string
'abc'
>>> delimiter = ' '
>>> letters_as_string = delimiter.join(letters)
>>> letters_as_string
'a b c'
>>> delimiter = '' #empty string
... 
>>> letters_as_string = delimiter.join(letters)
... 
>>> letters_as_string
'abc'
>>> len(letters_as_string)
3
>>> letters_as_string[1]
'b'
>>> 'abc' + '' + 'def'
'abcdef'
>>> delimiter = ',?!'
>>> delimiter.join(letters)
'a,?!b,?!c'
>>> delimiter_1 = ','
>>> delimiter_2 = '?'
>>> cat_name = 'whiskers'
>>> cat_name.join(letters)
'awhiskersbwhiskersc'
