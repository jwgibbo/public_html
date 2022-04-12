#main.py

#import the student class
from student import Student

def main():
    x = 5
    y = 10
    z = 99
    nums = [1, 2, 3, 4]
    letters = set('cowabunga')

    #implicity call to __init__
    my_stu = Student()
    my_stu2 = Student()
    
    my_stu.name = 'John Gibbons'
    my_stu.major = 'EECS'
    my_stu.gpa = 3.0
    my_stu.id = 1234567
    
    my_stu2.name = 'Juan Gibbons'
    my_stu2.major = 'CHEM'
    my_stu2.gpa = 4.0
    my_stu2.id = 1234568
    
    print(my_stu.name)
    print(my_stu.major)
    
    print(nums)

main()
    
