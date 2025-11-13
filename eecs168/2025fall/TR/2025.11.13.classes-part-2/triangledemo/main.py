#main.py

from triangle import Triangle

def main():
    my_tri = Triangle(5, 10) #call __init__
    your_tri = Triangle(25, 75)

    print('my_area =', my_tri.area())
    print('your area =', your_tri.area())

main()
