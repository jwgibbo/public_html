#main.py

from triangle import Triangle

def main():
    my_tri = Triangle(5, 10)
    your_tri = Triangle(5, 10)

    print(my_tri)
    print(your_tri)

    shapes = [my_tri, your_tri]
    print(shapes)
    

    if my_tri == your_tri:
        print('equal')
    else:
        print('not equal')

main()
