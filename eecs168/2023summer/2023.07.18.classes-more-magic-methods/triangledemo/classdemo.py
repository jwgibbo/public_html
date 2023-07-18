#classdemo.py

from triangle import Triangle

def main():
    my_tri = Triangle(2, 4)
    your_tri = Triangle(200, 400)

    print(my_tri)
    print(your_tri)

    triangle_list = [my_tri, your_tri]
    print(triangle_list)

main()
