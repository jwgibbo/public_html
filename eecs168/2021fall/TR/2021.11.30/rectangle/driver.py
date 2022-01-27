#driver.py
from rectangle import Rectangle

def main():
    rec1 = Rectangle(10,20)
    rec2 = Rectangle(2,3)

    print(rec1)
    print(rec2)

    recs = [rec1, rec2]

    #the list is passed to print
    #not the rectangles
    #invokes __repr__ on rectangles
    print(recs)

main()
