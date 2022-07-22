#main.py

from circle import Circle

def main():
    circ1 = Circle()
    circ2 = Circle()

    circ1.radius = 10
    circ2.radius = 10

    if circ1 < circ2:
        print('circ1 is smaller')
    else:
        print('circ1 is not smaller')

    if circ2 < circ1:
        print('circ2 is smaller')
    else:
        print('circ2 is not smaller')

    print(f'circ1 radius={circ1.radius}')
    print(f'circ2 radius={circ2.radius}')
    if circ1 == circ2:
        print('The circles are equal')
    else:
        print('They are not equal')

    print(circ1)

main()
