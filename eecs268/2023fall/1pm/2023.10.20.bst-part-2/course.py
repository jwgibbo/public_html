#course.py

class Course:
    def __init__(self, number, credit_hours, prof):
        self.course_number = number
        self.credit_hours = credit_hours
        self.prof = prof

    def __eq__(self, other):
        if isinstance(other, int):
            return self.course_number == other
        else:
            #Assume we got a Course
            return self.course_number == other.course_number
        
    def __lt__(self, other):
        if isinstance(other, int):
            return self.course_number < other
        else:
            #Assume we got a Course
            return self.course_number < other.course_number

    def __gt__(self, other):
        if isinstance(other, int):
            return self.course_number > other
        else:
            #Assume we got a Course
            return self.course_number > other.course_number
