#main.py
from triangle import Triangle

def main():
    my_tri = Triangle(10, 5)
    print(my_tri.area())

    your_tri = Triangle(20, 50)
    print(your_tri.area())

main()
