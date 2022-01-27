#driver.py

#when importing a class we made:
#from module import ClassName
from student import Student

def main():
    stu1 = Student() #calls __init__
    stu2 = Student() #calls __init__

    stu1.name = 'John'
    stu2.name = 'Susie'

    #Notice, only one parameter
    stu1.change_major('EECS')
    stu2.change_major('CHEM')
    change_major('ECON')
    print(stu1.major)
    print(stu2.major)


main()
