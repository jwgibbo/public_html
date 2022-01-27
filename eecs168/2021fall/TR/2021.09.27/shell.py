Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> word = "candy"
>>> word_as_list = list(word)
>>> word_as_list
['c', 'a', 'n', 'd', 'y']
>>> int(3.14159)
3
>>> len(word)
5
>>> len(word_as_list)
5
>>> str(word_as_list)
"['c', 'a', 'n', 'd', 'y']"
>>> len(str(word_as_list))
25
>>> print(word_as_list)
['c', 'a', 'n', 'd', 'y']
>>> some_string = ""
>>> len(some_string)
0
>>> some_string.join(word_as_list)
'candy'
>>> some_string = ","
>>> some_string.join(word_as_list)
'c,a,n,d,y'
>>> some_string = "ABC"
>>> some_string.join(word_as_list)
'cABCaABCnABCdABCy'
>>> delmiter = ",
SyntaxError: EOL while scanning string literal
>>> delimiter = ','
>>> delimiter.join(word_as_list)
'c,a,n,d,y'
>>> delimiter
','
>>> delimiter = '____'
>>> delimiter.join(word_as_list)
'c____a____n____d____y'
>>> delimiter = ""
>>> word = delimiter.join(word_as_list)
>>> word
'candy'
>>> my_list = [1,2,3]
>>> word = delimiter.join(my_list)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    word = delimiter.join(my_list)
TypeError: sequence item 0: expected str instance, int found
>>> user_name = input("Enter your name: ")
Enter your name: John Gibbons
>>> user_name
'John Gibbons'
>>> list(user_name)
['J', 'o', 'h', 'n', ' ', 'G', 'i', 'b', 'b', 'o', 'n', 's']
>>> user_name
'John Gibbons'
>>> name_list = user_name.split()
>>> name_list
['John', 'Gibbons']
>>> name_list[0]
'John'
>>> name_list[1]
'Gibbons'
>>> name_list
['John', 'Gibbons']
>>> delimiter
''
>>> delimiter = ' '
>>> name_string = delimiter.join(name_list)
>>> name_string
'John Gibbons'
>>> user_name = input("Enter your name: ")
Enter your name: John William Fitzgerland Highlander Orson Jebadiah Smith Creed Valentine Chimichummy Gibbons
>>> user_name
'John William Fitzgerland Highlander Orson Jebadiah Smith Creed Valentine Chimichummy Gibbons'
>>> user_name.split()
['John', 'William', 'Fitzgerland', 'Highlander', 'Orson', 'Jebadiah', 'Smith', 'Creed', 'Valentine', 'Chimichummy', 'Gibbons']
>>> print("Hello " + user_name[0] + ' ' + user_name[-1])
Hello J s
>>> user_name = user_name.split()
>>> user_name
['John', 'William', 'Fitzgerland', 'Highlander', 'Orson', 'Jebadiah', 'Smith', 'Creed', 'Valentine', 'Chimichummy', 'Gibbons']
>>> print("Hello " + user_name[0] + ' ' + user_name[-1])
Hello John Gibbons
>>> new_string.join(user_name)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    new_string.join(user_name)
NameError: name 'new_string' is not defined
>>> new_string = ''
>>> new_string.join(user_name)
'JohnWilliamFitzgerlandHighlanderOrsonJebadiahSmithCreedValentineChimichummyGibbons'
>>> "ABCDEFG".count("DEF")
1
>>> ' '.join(user_name)
'John William Fitzgerland Highlander Orson Jebadiah Smith Creed Valentine Chimichummy Gibbons'
>>> delmiter = ' '
>>> delimiter.join(user_name)
'John William Fitzgerland Highlander Orson Jebadiah Smith Creed Valentine Chimichummy Gibbons'
>>> delmiter
' '
>>> delimiter
' '
>>> delimiter.join(['a','b','c'] + ['d','e', 'f'])
'a b c d e f'
>>> delimiter.join(['a','b','c'],['d','e', 'f'])
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    delimiter.join(['a','b','c'],['d','e', 'f'])
TypeError: join() takes exactly one argument (2 given)
>>> delimiter.join("abc")
'a b c'
>>> comma = ','
>>> slash = '/'
>>> comma.join(slash.join(user_name))
'J,o,h,n,/,W,i,l,l,i,a,m,/,F,i,t,z,g,e,r,l,a,n,d,/,H,i,g,h,l,a,n,d,e,r,/,O,r,s,o,n,/,J,e,b,a,d,i,a,h,/,S,m,i,t,h,/,C,r,e,e,d,/,V,a,l,e,n,t,i,n,e,/,C,h,i,m,i,c,h,u,m,m,y,/,G,i,b,b,o,n,s'
>>> comma.join(" ")
' '
>>> result = ' '.split()
>>> result
[]
>>> grocery_list = "bread,fruit,milk"
>>> grocery_list.split(',')
['bread', 'fruit', 'milk']
>>> grocery_list = "bread,fruit,milk,"
>>> grocery_list.split(',')
['bread', 'fruit', 'milk', '']
>>> grocery_list
'bread,fruit,milk,'
>>> 