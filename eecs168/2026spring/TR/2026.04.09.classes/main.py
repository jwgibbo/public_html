#main.py

from triangle import Triangle

def main():
    my_tri = Triangle()
    your_tri = Triangle()
    print(my_tri)
    print('base =', my_tri.base)
    print('height =', my_tri.height)

    my_tri.base = 10
    my_tri.height = 20

    your_tri.base = 20
    your_tri.height = 32

    word = 'banana'
    print(word.upper())
    print(word.count('a'))
    print(upper())

    print(my_tri.area())
    print(your_tri.area())
    
    
main()
