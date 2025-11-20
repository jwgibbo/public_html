#main.py

from triangle import Triangle

def main():
    my_tri = Triangle(5, 10)
    your_tri = Triangle(5, 10)
    shapes = [my_tri, your_tri]
    print(my_tri)
    print(your_tri)
    print(shapes)

    
    #Goal: Make this work!
    if my_tri > your_tri:
        print('my tri is larger')
    else:
        print('my tri is NOT larger')

    #Without an __eq__ definition, python
    #uses an is comparison
    if my_tri == your_tri:
        print('equal')
    else:
        print('not equal')

main()
