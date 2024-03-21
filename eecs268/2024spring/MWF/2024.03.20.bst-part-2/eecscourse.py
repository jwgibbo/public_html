#eecscourse.py

class EECSCourse:
    def __init__(self):
        self.course_number = ???
        self.professor = ???
        self.credit_hours = ???
        self.difficulty = ???

    #other class methods

    def __lt__(self, other):
        return self.course_number < other.course_number
        #We'll add to this next time
