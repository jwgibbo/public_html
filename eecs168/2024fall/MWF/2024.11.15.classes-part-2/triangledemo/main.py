#main.py
from triangle import Triangle

def main():
    my_tri = Triangle()
    your_tri = Triangle()

    my_tri.base = 10
    my_tri.height = 5

    your_tri.base = 40
    your_tri.height = 120

    print(my_tri.area())
    print(your_tri.area())

    if my_tri.is_larger(your_tri):
        print('I have the bigger triangle')
    else:
        print('You have the bigger triangle')
main()
    
