#main.py
from circle import Circle

def main():
    my_circle = Circle()
    your_circle = Circle()
  
    my_circle.radius = 2.5
    your_circle.radius = 3.5
    #visualization #1 here

    print(my_circle.area())
    print(your_circle.area())
main()
