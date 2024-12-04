#main.py
from triangle import Triangle

def use_shape(some_shape):
    print('Printing the area:')
    print(some_shape.area())

def main():
    my_tri = Triangle(5, 10)
    use_shape(my_tri)

main()
