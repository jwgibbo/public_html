#main.py

from triangle import Triangle

def main():
    my_tri = Triangle()
    your_tri = Triangle()

    my_tri.base = 10
    my_tri.height = 20
    print('base =', my_tri.base)
    print('height =', my_tri.height)

    your_tri.base = 30
    your_tri.height = 40

    print(my_tri.area())
    print(your_tri.area())
main()
