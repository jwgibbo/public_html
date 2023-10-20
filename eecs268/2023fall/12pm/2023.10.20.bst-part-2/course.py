#course.py

#An example ItemType
class Course:
    def __init__(self, dept, number, hours, teacher):
        self.dept = dept      
        self.course_number = number #course number will be the key
        self.credit_hours = hours
        self.teacher = teacher

    def __eq__(self, other):
        if isinstance(other, int):
            return self.course_number == other
        else: #Assume we have Course object
            return self.course_number == other.course_number
        
    def __lt__(self, other):
        if isinstance(other, int):
            return self.course_number < other
        else: #Assume we have Course object
            return self.course_number < other.course_number
