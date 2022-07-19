#classdemo.py

from student import Student

def main():
    stu1 = Student()
    stu2 = Student()
    
    stu1.name = "John Gibbons"
    stu1.id = 12345
    stu1.gpa = 2.7

    stu2.name = 'Luna Gibbons'
    stu2.id = 6
    stu2.gpa = 4.0
    
    print(stu1.name)
    print(stu1.id)
    print(stu1.gpa)

    print(stu2.name)
    print(stu2.id)
    print(stu2.gpa)   

main()
