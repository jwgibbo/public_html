#main.py

from triangle import Triangle

def main():
    my_tri = Triangle()
    your_tri = Triangle()
    
    my_tri.base = 10
    my_tri.height = 20

    your_tri.base = 30
    your_tri.height = 15
    
    print(my_tri.base)
    print(my_tri.height)
    print('my_tri area =', my_tri.area())

    print('your_tri area =', your_tri.area())

main()
