#main.py
from student import Student

def main():
    stu1 = Student()
    stu1.name = 'luna'
    stu1.gpa = 4.0
    stu1.id = 7
    print(stu1.name)
    print(stu1.gpa)
    print(stu1.id)
    
    stu2 = Student()
    stu2.name = 'john'
    stu2.gpa = 2.7
    stu2.id = 12345

main()
