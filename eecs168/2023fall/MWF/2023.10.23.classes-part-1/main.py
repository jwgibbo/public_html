#main.py

from student import Student

def main():
    stu1 = Student()
    stu1.name = 'susie'
    stu1.age = 19
    stu1.id = 12345
    stu1.transcript()


    stu2 = Student()
    stu2.name = 'stevie'
    stu2.age = 18
    stu2.id = 54321
    stu2.gpa = 2.5
    stu2.transcript()


main()
