#EECS_Course


class EECS_Course:
    def __init__(self):
        self.course_num = ???
        self.prof = ???
        self.credits = ???
        self.required = ???

    def __lt__(self, other):
        #Key is an int
        #Entry is an EECS_Course object
        if isinstance(other, int):
            return self.course_num < other
        else:
            return self.course_num < other.course_num

    def __gt__(self, other):
        #More on this on Wednesday

    def __eq__(self, other):
        if isinstance(other, int):
            return self.course_num == other
        else:
            return self.course_num == other.course_num
