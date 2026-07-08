#eecscourse.py

class EECS_Course:
    def __init__(self, course_num, prof, credit_hours):
        self.course_num = course_num
        self.prof = prof
        self.credit_hours = credit_hours

    def __lt__(self, other):
        if isinstance(other, int):
            return self.course_num < other
        else:
            return self.course_num < other.course_num

    def __eq__(self, other):
        if isinstance(other, int):
            return self.course_num == other
        else:
            return self.course_num == other.course_num
    
    def __gt__(self, other):
        if isinstance(other, int):
            return self.course_num > other
        else:
            return self.course_num > other.course_num
