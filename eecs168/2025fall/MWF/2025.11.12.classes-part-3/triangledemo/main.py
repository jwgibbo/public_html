#main.py

from triangle import Triangle

def main():
    my_tri = Triangle(5, 10)
    your_tri = Triangle(20, 30)
    #my_tri.hiegth = 50
    #print('my hiegth =', my_tri.hiegth)
    #print('your hiegth =', your_tri.hiegth)
    
    print(my_tri.base)
    print(my_tri.height)
    print('my_tri area =', my_tri.area())

    print('your_tri area =', your_tri.area())

main()
