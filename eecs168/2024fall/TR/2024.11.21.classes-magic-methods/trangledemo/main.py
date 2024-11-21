#main.py
from triangle import Triangle

def main():
    my_tri = Triangle(5, 10) #__init__ called
    your_tri = Triangle(5, 10) #__init__ called

    print(my_tri.area())
    print(your_tri.area())

    
    if my_tri > your_tri:
        print('my_tri is larger')
    else:
        print('your_tri is larger')

    if my_tri == your_tri:
        print('same')
    else:
        print('different')

    print(my_tri)


main()
