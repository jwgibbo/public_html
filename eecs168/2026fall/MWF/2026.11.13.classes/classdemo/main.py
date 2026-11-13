#main.py

from triangle import Triangle

def main():
    my_tri = Triangle()
    your_tri = Triangle()

    my_tri.base = 5
    my_tri.height = 8

    your_tri.base = 3
    your_tri.height = 4

    print(my_tri.area())
    print(your_tri.area())

main()
