#main.py

#import the new class
from triangle import Triangle

def main():
    my_tri = Triangle()
    my_tri.base = 5.5
    my_tri.height = 10.2

    your_tri = Triangle()
    your_tri.base = 5.0
    your_tri.height = 7.0

    print(my_tri.base)
    print(my_tri.height)

    print(your_tri.base)
    print(your_tri.height)

    print(type(my_tri))

main()
