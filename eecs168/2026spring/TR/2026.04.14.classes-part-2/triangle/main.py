#main.py

from triangle import Triangle

def main():
    my_tri = Triangle(10, 20) #calls init
    your_tri = Triangle(20, 32) #calls init
    
    print(my_tri)
    print('base =', my_tri.base)
    print('height =', my_tri.height)
    word = 'banana'
    print(word.upper())
    print(word.count('a'))
    #print(upper())

    print(my_tri.area())
    print(your_tri.area())

    #   self             other
    if my_tri.is_larger(your_tri):
        print('My triangle is larger')
    else:
        print('My triangle is NOT larger')

    #    self              other
    if your_tri.is_larger(my_tri):
        print('Your triangle is larger')
    else:
        print('Your triangle is NOT larger')
        
    
main()
