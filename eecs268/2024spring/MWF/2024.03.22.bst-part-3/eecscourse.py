#eecscourse.py

class EECSCourse:
    def __init__(self):
        self.course_number = ???
        self.professor = ???
        self.credit_hours = ???
        self.difficulty = ???

    #other class methods

    def __lt__(self, other):
        if isinstance(other, int):
            return self.course_number < other
        else:
            return self.course_number < other.course_number
        
    def __gt__(self, other):
        return self.course_number > other.course_number
        #Add the isinstance if-else

    def __eq__(self, other):
        return self.course_number == other.course_number
        #Add the isinstance if-else
