class EECS_Course:
    def __init__(self, course_number, credit_hrs, prof):
        self.course_number = course_number
        self.credit_hrs = credit_hrs
        self.prof = prof

    def __lt__(self, rhs):
        if isinstance(rhs, int):
            return self.course_number < rhs
        else:
            return self.course_number < rhs.course_number

    def __gt__(self, rhs):
        if isinstance(rhs, int):
            return self.course_number > rhs
        else:
            return self.course_number > rhs.course_number

    def __eq__(self, rhs):
        if isinstance(rhs, int):
            return self.course_number == rhs
        else:
            return self.course_number == rhs.course_number
   
