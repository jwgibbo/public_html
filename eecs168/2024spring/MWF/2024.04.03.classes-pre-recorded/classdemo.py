#classdemo.py

from triangle import Triangle

def main():
    my_tri = Triangle()
    your_tri = Triangle()

    print(my_tri.base)
    print(my_tri.height)

    my_tri.base = 10
    my_tri.height = 150

    your_tri.base = 500
    your_tri.height = 25

    print(my_tri.base)
    print(my_tri.height)

    print(your_tri.base)
    print(your_tri.height)

    print(my_tri.area())
    print(your_tri.area())


main()
