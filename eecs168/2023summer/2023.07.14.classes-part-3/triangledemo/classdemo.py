#classdemo.py

from triangle import Triangle

def main():
    my_tri = Triangle(10, 150)
    your_tri = Triangle()

    print(my_tri.base)
    print(my_tri.height)

    print(my_tri.base)
    print(my_tri.height)

    print(your_tri.base)
    print(your_tri.height)

    print(my_tri.area())
    print(your_tri.area())


main()
