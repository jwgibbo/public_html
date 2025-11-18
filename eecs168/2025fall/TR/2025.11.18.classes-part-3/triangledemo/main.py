#main.py

from triangle import Triangle

def main():
    my_tri = Triangle(5, 10) #call __init__
    your_tri = Triangle(25, 75)

    if my_tri < your_tri:
        print('my tri is smaller')
    else:
        print('my tri is NOT smaller')

main()
