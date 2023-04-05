#main.py

from triangle import Triangle

def main():
    my_tri = Triangle()
    your_tri = Triangle()

    my_tri.base = 5
    my_tri.height = 10

    your_tri.base = 3
    your_tri.height = 4
    
    print('my base:', my_tri.base)
    print('my height:', my_tri.height)
    print('my area:', my_tri.area())
    print('your base:', your_tri.base)
    print('your height:', your_tri.height)
    print('your area:', your_tri.area())
main()
