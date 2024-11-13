#main.py
from triangle import Triangle

def main():
    my_tri = Triangle()
    your_tri = Triangle()

    my_tri.base = 10
    my_tri.height = 5

    your_tri.base = 4
    your_tri.height = 12
    
    print(type(my_tri))
    print(my_tri.base)
    print(my_tri.height)

    print(my_tri.area())
    print(your_tri.area())

main()
    
