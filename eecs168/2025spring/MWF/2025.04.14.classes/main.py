#main.py
from triangle import Triangle

def main():
    num = 5
    my_dict = dict()
    my_tri = Triangle()
    my_tri.base = 10
    my_tri.height = 5
    print(my_tri.base)
    print(my_tri.height)
    print(my_tri.area())
    


main()
