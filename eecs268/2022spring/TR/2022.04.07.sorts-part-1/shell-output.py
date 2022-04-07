Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nums = [1,2,3,4,5,6,7,8,9]
>>> evens = [num for num in nums]
>>> evens
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> evens = [num for num in nums if num%2==0]
>>> evens
[2, 4, 6, 8]
>>> doubles
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    doubles
NameError: name 'doubles' is not defined
>>> doubles = [num*2 for num in nums]
>>> doubles
[2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> even_cubes = [num**3 for num in nums if num%2==0]
>>> even_cubes
[8, 64, 216, 512]
>>> evens
[2, 4, 6, 8]
>>> nums
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> dict_of_cubes = {num: num**3 for num in nums}
>>> dict_of_cubes
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}
>>> dict_of_cubes[7]
343
>>> dict_of_cubes[9]
729
>>> odd_cube_dict = {num: cube for num, cube in dict_of_cubes.items()}
>>> odd_cube_dict
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}
>>> odd_cube_dict = {num: cube for num, cube in dict_of_cubes.items() if num%2==1}
>>> odd_cube_dict
{1: 1, 3: 27, 5: 125, 7: 343, 9: 729}
>>> my_tups = [('cat', 5) ('bat', 2)]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    my_tups = [('cat', 5) ('bat', 2)]
TypeError: 'tuple' object is not callable
>>> my_tups = [('cat', 5), ('bat', 2)]
>>> my_tups
[('cat', 5), ('bat', 2)]
>>> type(my_tups)
<class 'list'>
>>> type(my_tups[0])
<class 'tuple'>
>>> my_tups[0]
('cat', 5)
>>> KU_results = [(2022, 'champions!'), (2020, 'COVID'), (2018, 'final four')]
>>> year, result = KU_results[0]
>>> year
2022
>>> result
'champions!'
>>> 