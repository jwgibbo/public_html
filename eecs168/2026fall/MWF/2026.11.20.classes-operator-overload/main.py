#main.py

from triangle import Triangle

def main():
    my_tri = Triangle(5, 8)
    your_tri = Triangle(5, 8)

    print(my_tri.area())
    print(your_tri.area())

    if my_tri < your_tri:
        print('smaller')
    else:
        print('not smaller')

    if my_tri == your_tri:
        print('equal')
    else:
        print('not equal')

main()
