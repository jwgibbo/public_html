#main.py

from triangle import Triangle

def main():
    my_tri = Triangle()
    your_tri = Triangle()
    
    my_tri.base = 5.5
    my_tri.height = 10.5

    your_tri.base = 50
    your_tri.height = 100
    
    print(my_tri.base)
    print(my_tri.height)

    print(your_tri.base)
    print(your_tri.height)

    print(my_tri.area())
    print(your_tri.area())
    

main()
