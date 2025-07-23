#main.py

from shape import Shape
from triangle import Triangle

def main():
    my_shape = Shape()
    #print(my_shape.area())

    my_tri = Triangle(5, 10)
    print(my_tri.area())

main()
