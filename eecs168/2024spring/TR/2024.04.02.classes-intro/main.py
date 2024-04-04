#main.py

from triangle import Triangle

def main():
    my_tri = Triangle()
    your_tri = Triangle()    
    my_tri.base = 10
    my_tri.height = -20
    your_tri.base = 18
    your_tri.height = 2
    print(my_tri.area())
    print(your_tri.area())

main()
    
