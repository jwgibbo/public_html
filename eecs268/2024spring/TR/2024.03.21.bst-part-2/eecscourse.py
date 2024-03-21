#eecscourse.py

class EECS_Course:
    def __init__(self, ???):
        self.course_number = ???
        self.professor = ???
        self.credits = ???
        self.difficulty = ???

    #Any other methods

    def __lt__(self, other):
        if isinstance(other, int):
            return self.course_number < other
        else:
            return self.course_number < other.course_number

    def __gt__(self, other):
        #update with isinstance
        return self.course_number > other.course_number

    def __eq__(self, other):
        #update with isinstance
        return self.course_number == other.course_number
        
