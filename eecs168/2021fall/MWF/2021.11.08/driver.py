from student import Student

def main():
    #With what we currently know
    '''
    name = 'John'
    kuid = 12345
    gpa = 3.0
    major = 'CS'
    '''

    #Create a Student
    student1 = Student()
    
    #Access attributes
    student1.name = 'John'
    student1.kuid = 12345
    student1.gpa = 3.0
    student1.major = 'CS'

    #We can make lots of Students!
    student2 = Student()
    
main()
