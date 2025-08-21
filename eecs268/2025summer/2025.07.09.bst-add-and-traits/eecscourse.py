#eecscourse.py

class EECS_Course:
    def __init__(self, course_num, prof, credit_hours, difficulty):
        self.course_num = course_num
        self.prof = prof
        self.credit_hours = credit_hours
        self.difficulty = difficulty


    #other methods

    def __lt__(self, other):
        #if self is a Course and other is an int
        if isinstance(other, int):
            #used by search
            return self.course_num < other
        else:
            #used by add
            return self.course_num < other.course_num
        
        

    #Also define __gt__, __eq__
