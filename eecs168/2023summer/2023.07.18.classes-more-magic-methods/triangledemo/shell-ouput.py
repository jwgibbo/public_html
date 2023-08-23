Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\jwgib\OneDrive\Desktop\public_html\eecs168\2023summer\2023.07.18.classes-more-magic-methods\triangledemo\classdemo.py
<triangle.Triangle object at 0x000001CC7F93CE10>
<triangle.Triangle object at 0x000001CC7E8F3C90>

= RESTART: C:\Users\jwgib\OneDrive\Desktop\public_html\eecs168\2023summer\2023.07.18.classes-more-magic-methods\triangledemo\classdemo.py
Traceback (most recent call last):
  File "C:\Users\jwgib\OneDrive\Desktop\public_html\eecs168\2023summer\2023.07.18.classes-more-magic-methods\triangledemo\classdemo.py", line 12, in <module>
    main()
  File "C:\Users\jwgib\OneDrive\Desktop\public_html\eecs168\2023summer\2023.07.18.classes-more-magic-methods\triangledemo\classdemo.py", line 9, in main
    print(my_tri)
TypeError: __str__ returned non-string (type NoneType)

= RESTART: C:\Users\jwgib\OneDrive\Desktop\public_html\eecs168\2023summer\2023.07.18.classes-more-magic-methods\triangledemo\classdemo.py
Triangle: base=self.base height=self.height
Triangle: base=self.base height=self.height

= RESTART: C:\Users\jwgib\OneDrive\Desktop\public_html\eecs168\2023summer\2023.07.18.classes-more-magic-methods\triangledemo\classdemo.py
Triangle: base=2 height=4
Triangle: base=200 height=400

= RESTART: C:\Users\jwgib\OneDrive\Desktop\public_html\eecs168\2023summer\2023.07.18.classes-more-magic-methods\triangledemo\classdemo.py
Triangle: base=2 height=4
Triangle: base=200 height=400

= RESTART: C:\Users\jwgib\OneDrive\Desktop\public_html\eecs168\2023summer\2023.07.18.classes-more-magic-methods\triangledemo\classdemo.py
Triangle: base=2 height=4
Triangle: base=200 height=400
[repr called, repr called]

= RESTART: C:\Users\jwgib\OneDrive\Desktop\public_html\eecs168\2023summer\2023.07.18.classes-more-magic-methods\triangledemo\classdemo.py
Triangle: base=2 height=4
Triangle: base=200 height=400
[<triangle.Triangle object at 0x000001E075CA3C90>, <triangle.Triangle object at 0x000001E07806CE10>]

= RESTART: C:\Users\jwgib\OneDrive\Desktop\public_html\eecs168\2023summer\2023.07.18.classes-more-magic-methods\triangledemo\classdemo.py
Triangle: base=2 height=4
Triangle: base=200 height=400
[repr called, repr called]

= RESTART: C:\Users\jwgib\OneDrive\Desktop\public_html\eecs168\2023summer\2023.07.18.classes-more-magic-methods\triangledemo\classdemo.py
Triangle: base=2 height=4
Triangle: base=200 height=400
[Triangle(), Triangle()]
new_list_of_tris = [Triangle(), Triangle()]

= RESTART: C:\Users\jwgib\OneDrive\Desktop\public_html\eecs168\2023summer\2023.07.18.classes-more-magic-methods\triangledemo\classdemo.py
Triangle: base=2 height=4
Triangle: base=200 height=400
[Triangle(self), Triangle(self)]
>>> 
= RESTART: C:\Users\jwgib\OneDrive\Desktop\public_html\eecs168\2023summer\2023.07.18.classes-more-magic-methods\triangledemo\classdemo.py
Triangle: base=2 height=4
Triangle: base=200 height=400
[Triangle(self.base, self.height), Triangle(self.base, self.height)]
>>> 
= RESTART: C:\Users\jwgib\OneDrive\Desktop\public_html\eecs168\2023summer\2023.07.18.classes-more-magic-methods\triangledemo\classdemo.py
Triangle: base=2 height=4
Triangle: base=200 height=400
[Triangle(2, 4), Triangle(200, 400)]
>>> new_tris = [Triangle(2, 4), Triangle(200, 400)]
>>> new_tris
[Triangle(2, 4), Triangle(200, 400)]
>>> new_tris[0].area()
4.0
>>> new_tris[1].area()
40000.0
>>> nums = [5, 10, 15, 20]
>>> nums
[5, 10, 15, 20]
>>> new_nums = [5, 10, 15, 20]
>>> new_nums
[5, 10, 15, 20]
