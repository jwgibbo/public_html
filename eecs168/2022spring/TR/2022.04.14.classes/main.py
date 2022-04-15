#main.py

from circle import Circle

def main():
    #We made two Circle objects
    circ1 = Circle()
    circ2 = Circle()

    circ1.radius = 5.5
    circ2.radius = 6.3

    word1 = 'banana'
    print(word1.count('a'))
    
    print(circ1.area())
    print(circ1.circumference())

    print(circ2.area())
    print(circ2.circumference())

main()
