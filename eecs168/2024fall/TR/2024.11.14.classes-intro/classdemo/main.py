#main.py
from triangle import Triangle

def main():
    my_tri = Triangle()
    your_tri = Triangle()

    my_tri.base = 5
    my_tri.height = 10

    your_tri.base = 7
    your_tri.height = 11

    print(my_tri.area())
    print(your_tri.area())

    print(my_tri.is_larger(your_tri))


main()
