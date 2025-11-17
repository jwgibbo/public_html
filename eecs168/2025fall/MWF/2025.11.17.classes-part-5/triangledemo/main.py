#main.py

from triangle import Triangle

def main():
    my_tri = Triangle(5, 10)
    your_tri = Triangle(5, 10)
    #Goal: Make this work!
    if my_tri > your_tri:
        print('my tri is larger')
    else:
        print('my tri is NOT larger')

    if my_tri == your_tri:
        print('equal')
    else:
        print('not equal')

main()
