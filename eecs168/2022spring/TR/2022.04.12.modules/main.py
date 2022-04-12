#main.py

import gibutilities
from student import Student

def main():
    x = 5
    word = 'doggy'

    print("did you know that 2+1 is...")
    print(gibutilities.one_more(2))

    #Create a variable of type Student
    #Implicit call to __init__
    my_stu = Student()
    my_stu2 = Student()

    my_stu.name = 'John Gibbons'
    my_stu.id = 1234567
    my_stu.gpa = 2.9
    my_stu.major = 'EECS'
    
    my_stu2.name = 'Juan Gibbons'

    print(my_stu.name)
    print(my_stu2.name)

main()
