#main.py

from triangle import Triangle

def main():
    my_tri = Triangle()
    your_tri = Triangle()
    
    my_tri.base = 50
    my_tri.height = 10

    your_tri.base = 50
    your_tri.height = 10
    
    print(my_tri.base)
    print(my_tri.height)

    print(your_tri.base)
    print(your_tri.height)

    print(my_tri.area())
    print(your_tri.area())

    #implicit call to __gt__
    if my_tri > your_tri:
        print('my_tri is larger')
    else:
        print('my_tri is not larger')

    if my_tri == your_tri:
        print('they are equal')
    else:
        print('they are different')

    print(my_tri)
    print(your_tri)

main()
