#main.py
from triangle import Triangle

def main():
    my_tri = Triangle(1000, 5000)
    print(my_tri.area())

    your_tri = Triangle(20, 50)
    print(your_tri.area())

    if my_tri.is_larger(your_tri):
        print('my_tri is larger')
    else:
        print('your_tri is larger (or equal)')

main()
