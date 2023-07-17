#classdemo.py

from triangle import Triangle

def main():
    my_tri = Triangle(2, 4)
    your_tri = Triangle(200, 400)

    print(my_tri.area())
    print(your_tri.area())

    if my_tri < your_tri:
        print('my_tri is smaller')
    else:
        print('my_tri is not smaller')

    if your_tri < my_tri:
        print('your_tri is smaller')
    else:
        print('your_tri is not smaller')

    test_tri1 = Triangle(5, 10)
    test_tri2 = Triangle(5, 10)
    
    test_tri3 = test_tri2

    if test_tri1 == test_tri2:
        print('test tri 1 and 2 are the same')
    else:
        print('test tri 1 and 2 are not the same')

    if test_tri2 == test_tri3:
        print('test tri 2 and 3 are the same')
    else:
        print('test tri 2 and 3 are not the same')

main()
