#main.py
from triangle import Triangle
from circle import Circle

def main():
    my_tri = Triangle(5, 10)
    my_circle = Circle(100)
    
    print(my_tri.area())
    print(my_circle.area())

main()
