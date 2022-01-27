#driver.py
from student import Student

def main():
    #With what we know...
    '''
    name = 'John'
    kuid = 12345
    gpa = 3.0
    major = 'EECS'
    '''

    #Creating new Student
    stu1 = Student('John', 12345)
    stu2 = Student('Mandy', 54321)
    
    #Give the attributes values
    #stu1.name = 'John'
    #stu1.kuid = 12345
    stu1.gpa = 3.0
    stu1.major = 'EECS'

    #stu2.name = 'Mandy'
    #stu2.kuid = 54321
    stu2.gpa = 4.0
    stu2.major = 'MATH'

    print(stu1.name, ' ' , stu1.gpa)
    print(stu2.name, ' ' , stu2.gpa)

    #Notice there's only 1 parameter?
    stu1.change_major('COOK')
    stu2.change_major('ECON')


main()
    
