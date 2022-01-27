#student.py

class Student:
    
    def __init__(self, name, kuid):
        #define the attributes our
        #class has and their default value
        self.name = name
        self.kuid = kuid
        self.gpa = 0.0
        self.major = ''

    def change_major(self, new_major):
        self.major = new_major
        
    
