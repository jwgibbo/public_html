#main.py

from triangle import Triangle

def main():
    word = 'bird'
    title = 'eecs 168'
    num = 2.5
    my_tri = Triangle()
    your_tri = Triangle()
    print(type(word))
    print(type(num))
    print(type(my_tri))
    my_tri.base = 10
    my_tri.height = 20
    your_tri.base = 8
    your_tri.height = 9
    print(my_tri.base, my_tri.height)
    print(your_tri.base, your_tri.height)

    print(word.upper())
    print('my area =', my_tri.area())
    print('your area =', your_tri.area())
main()
